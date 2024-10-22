import csv
csvtransformed = open('../data/data_transformed.csv', 'w', newline='', encoding="utf8")
id = 0
with open('../data/data.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    spamwriter = csv.writer(csvtransformed, delimiter=',')
    entete = False
    for row in spamreader:
        if not entete:
            spamwriter.writerow(["Id",row[0],row[1],row[2],row[3],row[4],row[5],row[6],"Venue","City","Country",row[8],"Result_Score",row[11],row[12]])
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
            ville = ville.replace("é","e")
            ville = ville.replace("è","e")
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
            spamwriter.writerow([id,row[0],row[1],row[2],nom,row[4],row[5],row[6],stade,ville,pays,row[8],row[9],sport,row[12]])