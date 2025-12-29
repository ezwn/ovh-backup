
Division Euclidienne

Divisibilité [00:00:00]:
    - diviseur commun à deux nombre => diviseur de leur somme
    - division euclidienne [00:03:36]

PGCD [00:07:15]:
    - PGCD(a, b) = 1 <=> a et b premiers entre eux.
    - Par l'algorithme d'Euclide [00:11:10]:
      - Application [00:15:36]

Nombres premiers entre eux [00:19:37]
Théorème de Bézout : ∃ u,v ∈ Z | a*u + b*v = pgcd(a, b) [00:21:48]
    - Corollaire : a, b premiers entre eux <=> ∃ u,v | au + bv = 1 [00:28:48]
    - Exemple [00:34:16]
    - Corollaire #2 :  d|a et d|b => d|pgcd(a,b) [00:34:35]
    - Corollaire #3 (Lemme de Gauss) : a|bc et pgcd(a, b)=1 alors a|c  [00:35:45]

PPCM [00:39:16]
    - Et PGCM : pgcd(a, b) * ppcm(a, b) = |a * b| [00:40:20]

Nombres premiers [00:43:00]:
    - Définition : ATTENTION: >=2
    - Lemme : tout entier admet un diviseur premier[00:47:42]
    - Crible d'Ératosthène [00:51:52]
    - Lemme d'Euclide : p | ab => p|a ou p|b [00:57:57]
    - Decomposition entiers produit de puissances de nombres premiers [01:06:40]:
      - Théorème existance unique décomposition [01:06:40]
      - Technique [01:07:25] : division par nombre premiers croissants jusqu'à reste 1.
      - Pour déterminer PGCD et PPCM [01:09:27] : écriture sous même produit de facteurs + conserver plus petits (PGCD), plus grands (PPCM)

Congruences [01:12:02]
    - Définition: n ≥ 2, a congruent à b modulo n, ssi n | a - b
        - on note: a ≡ b [n] ou a ≡ b (mod n)
    - a≡b[n] <=> ∃k∈ℤ, a=b+kn
    - a≡0[n] <=> n|a [01:16:00]
    - un nombre est congru à son reste modulo son diviseur [01:17:19]
    - la congruence est une relation d'équivalence (réflexive, transitive, symétrique)
    - propriétés [01:18:44]
      - a≡b [n] ⋏ c≡d [n]
        => a+c≡b+d [n]
        => a*c≡b*d [n]
        => a^k≡b^k [n]
      - exemple 1 [01:19:36]
      - exemple 2 [01:24:58] (divisibilité par 9)
      - 
# EXERCICES

| N°  | PROBLEMES                                                   | DATE       |
| --- | ----------------------------------------------------------- | ---------- |
| 01  | 1. j'ai voulu le démonter, alors qu'il suffisait d'observer | 2023-07-03 |
| 02  |                                                             | 2023-07-03 |
| 03  |                                                             | 2023-07-03 |
| 04  |                                                             | 2023-07-04 |
| 05  |                                                             | 2023-07-05 |
| 06  | Erreur d'attention                                          | 2023-07-06 |
| __  | 2. NOK                                                      | 2023-07-07 |
| 07  | 2. NOK                                                      | 2023-07-07 |
| __  | 3. Laborieux + erreurs d'attention                          | 2023-07-07 |
| 08  | Mauvaise utilisation probas                                 | 2023-07-07 |
| 09  | Relire immédiatement                                        | 2023-07-10 |