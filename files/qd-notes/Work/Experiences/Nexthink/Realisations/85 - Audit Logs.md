# Audit logs

## Analyse

La tâche consiste à créer le premier log d'audit. Ces logs sont destinés à l'utilisateur final pour lui permettre d'effectuer un diagnostic métier : qui, a fait quoi et à quel moment.

Le service fournissant l'infrastructure logicielle externe à mon équipe ne fournit pas de librairie.

Le code des autres équipes a été passé en revue : plusieurs ont déjà développé leur version spécifique (le code n'est pas réutilisable mais fournit des examples précieux).

Le surcout d'une solution générique n'est pourtant pas important et apporte également des bénéfices en terme de ré-utilisabilité et de séparation des responsabilités.

## Conception

* Design d'un modèle unifié (UML + Pojos) permettant de créer facilement des logs et de les valider.
  * Générateur de code à partir des événements. En effet chaque log a un code qui contient sa catégorie, le type d'action, l'objet sur lequel il porte, etc.
  * Générateur de description (clé=valeurs séparés par virgules) à partir de POJOs en utilisant la réflexivité. Choix difficile entre un hashmap ou POJO + réflexivité.  Seconde solution choisie car validation plus forte.
* Service d'envoi des événements dans la stream kafka.

(voir model quickdia)

## Coding

Le service converti l'évènement en sa version "proto" utilisée dans la stream kafka et l'envoie.

```java
public class AuditLogsService {

  @Property(name = "audit-log.kafka-topic-prefix")
  String auditLogsTopicPrefix;

  private final AuditLogsKafkaProducer auditLogsKafkaProducer;

  public void send(String tenantUuid, AuditEvent auditEvent) {
    log.debug("Sending an audit event tenantUuid={}", tenantUuid);
    log.debug("its code: {}", auditEvent.code());
    log.debug("its description: {}", auditEvent.description());

    AuditLog auditLog =
        AuditLog.newBuilder()
            .setFeature(auditEvent.getCategory().name())
            .setUser(auditEvent.getUserName())
            .setDescription(auditEvent.description())
            .setCode(auditEvent.code())
            .build();
    final var tenantAuditTopic = auditLogsTopicPrefix + tenantUuid;
    auditLogsKafkaProducer.sendAuditLog(tenantUuid, tenantAuditTopic, auditLog.toByteArray());
  }
}
```

Générer la description à partir des objets par reflexivité. Un peu complexe mais bien isolé.

```java
public class AuditDescriptionBuilder {

  private AuditDescriptionBuilder() {}

  public static String objectToDescriptionKeyValues(Object obj) {
    if (obj == null) {
      throw new IllegalArgumentException("Object cannot be null");
    }

    Class<?> clazz = obj.getClass();
    Field[] fields = clazz.getDeclaredFields();

    return Arrays.stream(fields)
        .filter(field -> hasGetter(clazz, field))
        .sorted(Comparator.comparing(AuditDescriptionBuilder::getKeyName))
        .map(
            field -> {
              String key = getKeyName(field);
              String value = getFieldValue(obj, field);
              return key + "=" + value;
            })
        .collect(Collectors.joining(", "));
  }

  private static boolean hasGetter(Class<?> clazz, Field field) {
    String capitalizedFieldName = capitalize(field.getName());
    String getterName = "get" + capitalizedFieldName;
    try {
      Method getter = clazz.getMethod(getterName);
      return getter != null;
    } catch (NoSuchMethodException e) {
      return false;
    }
  }

  private static String getKeyName(Field field) {
    CustomKey annotation = field.getAnnotation(CustomKey.class);
    return (annotation != null) ? annotation.value() : field.getName();
  }

  @SneakyThrows
  private static String getFieldValue(Object obj, Field field) {
    String capitalizedFieldName = capitalize(field.getName());
    String getterName = "get" + capitalizedFieldName;
    Method getter = obj.getClass().getMethod(getterName);
    Object value = getter.invoke(obj);
    return (value != null) ? value.toString() : "null";
  }

  private static String capitalize(String str) {
    if (str == null || str.isEmpty()) {
      return str;
    }
    return StringUtils.capitalize(str);
  }
}
```

## Implantation (usage)

```java
  private void sendApiTriggerCampaignAuditEvent(
      String jwtToken, CampaignDoc campaignDoc, Collection<String> sids) {
    Optional<JwtTokenInfo> tokenInfoOptional = triggerValidationService.getTokenInfo(jwtToken);
    tokenInfoOptional.ifPresent(
        tokenInfo ->
            auditLogs.send(
                tokenInfo.getTenantUid(),
                ApiTriggerCampaignEvent.builder()
                    .userName(tokenInfo.getSub())
                    .context(
                        AbstractCampaignEvent.CampaignContext.builder()
                            .id(campaignDoc.getNqlId())
                            .name(
                                campaignDoc.getName()
                                    + " "
                                    + String.format(
                                        "on %s users with SIDs: %s",
                                        sids.size(),
                                        sids.stream().collect(Collectors.joining(" - "))))
                            .build())
                    .build()));
  }
```