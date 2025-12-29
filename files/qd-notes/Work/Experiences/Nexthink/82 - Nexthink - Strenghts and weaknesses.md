# **Nexthink**

## **Strengths**

### **Management**

* Points réguliers (manager), démarche d'amélioration individuelle, formation intégrée à l'activité
* Parvenir à synchroniser autant de travailleurs
* Feedback vers les employés sur la situation de l'entreprise (fake?)
* Respecter la durée des réunions
* Confort des salariés, ouverture au télétravail, flexibilité

### **Technics**

#### Maîtrise de l'**architecture cloud**, Kafka.

#### **IA** ?

## **Weaknesses**

### **Organization**

#### **Pas de structure / standardisation**

* Il faudrait documenter le processus de prise de décision dans l'équipe.
  * En effet tous les membres en ont une perception différente.
* Les rôles ne sont pas clairement définis.
* Favoritisme ressenti n+1
* Non respect de la méthodologie SCRUM. Ex: changement d'objectifs en cours de sprint.
* Fausse démocratie parfois, tendance à manipuler
* finalement peu d'entraide spontané
* environnement humain complexe et finalement individualiste

### **Technical implementation**

#### **Inconsistance et désorganisation technique**

* Raison: trop consensualité technique
  * exemple: le métier qui dicte la technique : garder du code inutile (composant React non accédés), nommer une variable (triggeredOn)
  * tech-lead humain, mais désordonné
* Non respect des standards fondamentaux
  * validation des données
  * immutabilité des stream Kafka
  * principes SOLID, design patterns, clean code
* Faiblesse des guidelines
  * peu nombreuses
  * non respectées
  * résolue localement : conflits + incohérence globale
* Inconsistance technique structurelle
  * en termes de choix technologiques : redondance (graphql, rest, proto), choix personnels locaux
  * termes de nommage (projets, artéfacts, ...), et précision conceptuelle

#### **Faible stratégie technique globale**

* Détecter trop tard les problématiques transversales/génériques

#### **Petits problèmes techniques**

* Mauvais environnement de développement (builds long, instables, documentation mal centralisé : outils, urls pas clairs)
* Mac obligatoire, torture pour les autres