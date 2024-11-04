# Web Sémantique

## Membre du Groupe

| Basquin Nicolas |
| Danneaux Lucas |

## Slides de présentation du projet

[Google Slides du projet](https://docs.google.com/presentation/d/1b_Bj5HaflzAHDLpObsYDBm_gTWdTbdy5j4HuAsDxfis/edit#slide=id.g3072222d657_0_8)

## Dataset utilisés
- **Intitulé** : World Athletics Database
- **Source** : https://github.com/thomascamminady/world-athletics-database

## Mise à jour du Dataset
La source de données de base n'est pas à jour et contient beaucoup trop de données pour être exploitable.
La décision de mettre à jour les données de la base tout en réduisant le nombre de données à été prise.

les catégories qui seront conservés seront les suivantes :

- 100 Mètres (Homme/Femme)
- 200 Mètres (Homme/Femme)
- 400 Mètres (Homme/Femme)
- 100 Mètres Haies (Homme)
- 110 Mètres Haies (Femme)
- 400 Mètres Haies (Homme/Femme)

Les données récoltés auront comme période du 1/1/2024 au 22/10/2024.


### Exécution des commandes dans le répertoire world-athletics-database-main
#### Récupération des données
- `env\Script\activate`
- `python world_athletics_database/parse.py`
- `python world_athletics_database/postprocess.py`
#### Transformation des données
Certaines données récupérés sont reformatés afin de pouvoir être plus facilement exploité dans la suite du projet.

- `python transform.py`

## Sémantisation des données
Assembler l'outil tarql qui sera manipuler à l'aide de l'outil Maven
- `PS C:\Users\lucas\Downloads\Web Sémantique\tarql> mvn package appassembler:assemble`

Utilisation de l'outil Tarql pour sémantiser les données
- `.\tarql\target\appassembler\bin\tarql .\transform.sparql .\data\data_transformed.csv > .\athletics.ttl`

Le résultat de la sémantisation des données est le fichier [athletics.ttl](athletics.ttl) qui contient plus de 160 000 triplets. 
Il devient alors de réaliser des requêtes à l'aide d'un serveur fuseki.

## Lancer le server Fuseki local
`PS C:\apache-jena-fuseki-5.1.0> java -jar .\fuseki-server.jar` 

## Resource utilisés
- [Outil Tarql](https://tarql.github.io/)
- [Dataset](https://www.kaggle.com/datasets/mexwell/world-athletics-database)
- [Github du projet de récupération de données](https://github.com/thomascamminady/world-athletics-database)