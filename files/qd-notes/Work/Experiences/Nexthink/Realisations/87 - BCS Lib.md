# BCS Lib

## Le client générique

Lorsque nous avons eu besoin d'un client BCS REST, j'ai constaté qu'il était peu coûteux et bon pour la maintenabilité de créer un client générique. Cela permettait en effet de séparer correctement notre domaine métier et la logique d'accès à BCS. De plus, nous gérons deux entités métier (campagne et branding). Il pourrait par la suite devenir intéressant de réutiliser le même code.

J'en ai présenté l'idée au tech lead de Engage qui a proposé une collaboration à BCS pour développer un client réutilisable par toutes les équipes. Cependant BCS a décliné l'offre, préférant se concentrer sur la génération automatique du code de ce client, qui malheureusement n'a été disponible que bien plus tard, alors que nous avions déjà été obligés de développer notre version.

## L'import/export

Par la suite le besoin d'importer et exporter des documents (campagnes dans notre cas) par le biais d'une API, est apparu. Une spécification de l'API a été fournie car cette fonctionnalité est utilisée pour tous les types de documents.

Il est donc apparu que d'une part, le système source des données (BCS) et le système consommateur étaient indépendants des domaines métiers. Ainsi, il était possible de développer un mécanisme d'import/export agnostic par rapport au type de documents, ne délégant à la partie spécifique que la conversion entre les deux formats.

C'est un ainsi que nous avons construit un service générique d'import/export.

Il faut comprendre que la valeur ajoutée de ce service est bien plus importante qu'un simple client puisque la procédure d'import, par exemple, est en réalité un processus complexe supportant plusieurs modes (ajout, remplacement, simulation) et se comportant de façon standardisée en cas de problèmes ou par rapport aux messages retournés. Le développement et par la suite l'évolution synchrone de cette fonctionnalité est donc coûteux et le développement d'un service générique en amont aurait pu diviser ce coût par le nombre d'équipes, voir de types de documents, ce qui est considérable !

Nous avons développé ce service en nous appuyant sur le client générique décrit dans la partie précédente.

## L'extraction

Bien plus tard, au détour d'une conversation, j'ai présenté notre travail à l'architecte, qui a été convaincu par l'idée et m'a poussé à extraire le code dans une librairie à l'échelle de Nexthink.

Entre temps, BCS a proposé sa génération automatique du client, mais à ma connaissance il n'existe pas encore d'import/export générique et les équipes ont chacune développé leur propre version.

## Conclusion

En s'appuyant sur des composants génériques, il serait possible, non seulement de fortement réduire les efforts à fournir aujourd'hui pour développer des fonctionnalités transversales, mais également les coûts de maintenance et de synchronisation futurs. Pour cela, il faudrait anticiper suffisamment l'émergence de ces fonctionnalités et développer des composants génériques en amont, peut-être avec une ou des équipes pilotes. Malheureusement l'approche actuelle consiste plus à développer séparément, puis à unifier, ce qui, de mon point de vue, est souvent utopique, mais toujours bien plus coûteux.