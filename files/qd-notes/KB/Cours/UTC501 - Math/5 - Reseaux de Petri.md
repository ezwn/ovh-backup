
# COURS

- Elements:
    - Transactions
      - validée = franchissable [00:13:40]
      - tirer = franchir
    - Marquage
- Matrices
  - Pre : valuation arc entrants
  - Post : valuation arc sortants
  - d'incidence (C = Post - Pre) [00:15:40]
- Reseaux purs et impurs : Pre * Post = 0, boucle [00:27:30]
- Franchissabilité [00:30:00]
- Transition source et puit [00:30:50]
- Franchissement et évolution du marquage (calcul matriciel) [00:33:50]
  - Marquage: matrice colonne
  - M1 = M0 + col(C, transition)
- Relations entre transactions:
  - en conflit structurel : elles partagent des places pre
  - en conflit structurel et effectif : les ressources obligent à choisir une seule transaction
  - en concurrence : pas de conflit + franchissables
- Propriété réseaux:
  - vivace : toute transaction peut être validée et tirée par une séquence finie de franchissements
  - sain : marquage borné à 1
  - conforme : vivace et sain => pur
  - pur : ∀ p∈P, ∀t∈T, Pre(p,t).Post(p,t)=0
- Séquences de franchissement: [00:39:00]
    - S barre, Vecteur caractéristique (colonne) : nbr de fois que chaque transition appliquée (commutatif = ordre négligé).
    - Marquage final : M' = M + C.S [00:44:00]
    - S'il existe S non nul, tel que C.S=0 (donc M0 + C.S = M0), il existe un cycle dans l'évolution des marquages
- Arbre et graphe de couverture: [00:55:00]
    - Construction arbre couv par méth. de Karp et Miller
      - marquage état "old": déjà rencontré
      - marquage place "ω": stt supérieur précédent et continue [01:06:00]
      - marquage état "dead-end"
    - Théorème Karp: tout arbre est fini (tous old ou dead-end)
    - Graphe de couverture à partir de l'arbre de couverture [01:07:35]
    - Théorème: séquence franchissable ⟺ existence de chemin

- Invariant de marquage [1'12'00]
    - = toujours même nbr jetons dans un ensemble de places
    - p-semi-flot: vecteur ligne f (de places) | f*C=0 ∧ f≠0 [1'12'50]
    - M' = M + C.S => f.M' = f.M + f.C.S => f.M' = f.M [1'16'10]
    - proposition: f: p-semi-flot, M0: marquage initial, ∀ M: marquage accessible, f * M0 = f * M  [1'17'30]
      - En développant on obtient l'invariant

- Produits matriciels

# EXERCICES

| N°  | RESULTAT                            | DATE       |
| --- | ----------------------------------- | ---------- |
| 01  | ERREURS D'ATTENTION + DIFFICULTE 7. | 2023-06-12 |
| 02  | __                                  | 2023-06-15 |