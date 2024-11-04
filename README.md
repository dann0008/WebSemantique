# Web Sémantique

## Membre du Groupe

| Basquin Nicolas |
| Danneaux Lucas |

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
Mise en place en cours
- `PS C:\Users\lucas\Downloads\Web Sémantique\tarql> mvn package appassembler:assemble`
Utiliser l'outil Tarql pour sémantiser les données
- `.\tarql\target\appassembler\bin\tarql .\transform.sparql .\data\data_transformed.csv > .\test.ttl`

## Lancer le server Fuseki local
`PS C:\apache-jena-fuseki-5.1.0> java -jar .\fuseki-server.jar`

## Resource utilisés
- [Outil Tarql](https://tarql.github.io/)
- [Dataset](https://www.kaggle.com/datasets/mexwell/world-athletics-database)
- [Github du projet de récupération de données](https://github.com/thomascamminady/world-athletics-database)

#Note 
https://github.com/DjibSan/semantic-data-project/blob/main/script_change_csv_ttl.py
https://github.com/YannisCHUPIN/SemanticWebProject/blob/main/convert_csv_to_rdf.py

í
