# Sprint 1

## Objectif

- disposer d'un pilote de l'email, envoyé aux participants pour feedbacks.

## Tâches (⚡SP: 25)

- **Créer un plan de test et tester l'envoi d'emails ciblés par groupes métiers**  ⚡SP: 3

- **Modifier le workflow d'envoi d'email pour préparer un email par groupe métier** ⚡SP: 3

- **Modifier le workflow "consolidation" pour associer chaque offre à des groupe métiers en base** ⚡SP: 5

- **Migration de google sheet vers supabase et support des groupes métiers** ⚡SP: 5

- **Créer les listes de diffusions pour abonnement aux groupes métiers** ⚡SP: 3

- **Informations supplémentaires sur les offres** ⚡SP: 2

- **Mise en forme de l'email**  ⚡SP: 1

- **"veilleemploi" comme expéditeur dans workflow d'envoi**  ⚡SP: 3

### Séquence

```plantuml
@startgantt

[1. Mig GSheet→Supabase] as [MIG] lasts 20 days
[2. Listes diffusions] as [LIST] lasts 10 days
[3. WF consolidation] as [CONS] lasts 8 days
[4. WF envoi email] as [SEND] lasts 8 days
[5. Plan de tests et tests] as [TEST] lasts 10 days

[CONS] starts at [MIG]'s end
[SEND] starts at [MIG]'s end
[SEND] starts at [LIST]'s end
[TEST] starts at [CONS]'s end
[TEST] starts at [SEND]'s end

@endgantt
```
