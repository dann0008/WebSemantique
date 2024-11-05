import csv
csvtransformed = open('../data/data_transformed.csv', 'w', newline='', encoding="utf8")
id = 0
with open('../data/data.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    spamwriter = csv.writer(csvtransformed, delimiter=',')
    entete = False
    for row in spamreader:
        if not entete:
            spamwriter.writerow(["Id",row[0],row[1],row[2],"URI_Name",row[3],row[4],row[5],row[6],"Venue","City","Country",row[8],"Result_Score",row[11],row[12]])
            entete = True
        else:
            id += 1
            mot = ""
            nom = ""
            row[3] += " "
            for i in row[3]:
                if i == " ":
                    mot = mot.capitalize()
                    nom += f"{mot}_"
                    mot = ""
                elif i == "'":
                    mot = mot.capitalize()
                    nom += f"{mot}'"
                    mot = ""
                else:
                    mot += i
            nom = nom[:-1]
            pays = ""
            mot = ""
            stade = ""
            ville = ""
            flag = False
            flag2 = False
            for i in row[7]:
                if i == "," and not flag:
                    stade = mot
                    flag = True
                    mot = ""
                elif i == "," and flag == True and not flag2:
                    ville = mot
                    flag2 = True
                    mot = ""
                elif i == "(" and not flag2 and not flag:
                    ville = mot[:-1]
                    flag = ""
                    flag2 = True
                    mot = ""
                elif i == "(" and not flag2:
                    ville = mot[1:-1]
                    flag2 = True
                    mot = ""
                elif i == "(":
                    mot = ""
                else:
                    mot += i

    # Création d'une exception pour l'athlète Sydney Mclaughlin-levrone qui est un cas trop complexe à gerer
            if nom == "Sydney_Mclaughlin-levrone":
                nom = "Sydney_McLaughlin-Levrone"
    # Suppression de tous les caractères spéciaux causant des problèmes d'affichage
            ville = ville.replace("é","e")
            ville = ville.replace("è","e")
            ville = ville.replace("ê","e")
            ville = ville.replace("ë","e")
            ville = ville.replace("É","E")
            ville = ville.replace("Ê","E")
            ville = ville.replace("Ë","E")
            ville = ville.replace("È","E")
            ville = ville.replace("à","a")
            ville = ville.replace("À","a")
            ville = ville.replace("û","u")
            ville = ville.replace("ü","u")
            ville = ville.replace("ç","c")
            stade = stade.replace("é","e")
            stade = stade.replace("è","e")
            stade = stade.replace("ê","e")
            stade = stade.replace("ë","e")
            stade = stade.replace("É","E")
            stade = stade.replace("Ê","E")
            stade = stade.replace("Ë","E")
            stade = stade.replace("È","E")
            stade = stade.replace("à","a")
            stade = stade.replace("À","a")
            stade = stade.replace("û","u")
            stade = stade.replace("ü","u")
            stade = stade.replace("ç","c")
            nom = nom.replace("é","e")
            nom = nom.replace("è","e")
            nom = nom.replace("ê","e")
            nom = nom.replace("ë","e")
            nom = nom.replace("É","E")
            nom = nom.replace("Ê","E")
            nom = nom.replace("Ë","E")
            nom = nom.replace("È","E")
            nom = nom.replace("à","a")
            nom = nom.replace("À","a")
            nom = nom.replace("û","u")
            nom = nom.replace("ü","u")
            nom = nom.replace("ç","c")
            pays = mot.replace("(","").replace(")","")
            row[11] = row[11].replace("\\"," ")
            if row[11] == "Men 100 Metres":
                sport = "100_metres"
            if row[11] == "Men 110 Metres Hurdles":
                sport = "110_metres_hurdles"
            if row[11] == "Men 400 Metres Hurdles":
                sport = "400_metres_hurdles"
            if row[11] == "Men 200 Metres":
                sport = "200_metres"
            if row[11] == "Men 400 Metres":
                sport = "400_metres"
            if row[11] == "Women 100 Metres":
                sport = "100_metres"
            if row[11] == "Women 100 Metres Hurdles":
                sport = "100_metres_hurdles"
            if row[11] == "Women 400 Metres Hurdles":
                sport = "400_metres_hurdles"
            if row[11] == "Women 200 Metres":
                sport = "200_metres"
            if row[11] == "Women 400 Metres":
                sport = "400_metres"
            nom_uri = nom
            nom = nom = nom.replace("_"," ")
            spamwriter.writerow([id,row[0],row[1],row[2],nom_uri, nom, row[4],row[5],row[6],stade,ville,pays,row[8],row[9],sport,row[12]])