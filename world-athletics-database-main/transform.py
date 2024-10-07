import csv
csvtransformed = open('../data/data_transformed.csv', 'w', newline='', encoding="utf8")
with open('../data/data.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    spamwriter = csv.writer(csvtransformed, delimiter=';')
    entete = False
    for row in spamreader:
        if not entete:
            spamwriter.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],"Venue","City","Country",row[8],row[9],"Mark",row[11],row[12]])
            entete = True
        else:
            mot = ""
            nom = ""
            row[3] += " "
            for i in row[3]:
                if i == " ":
                    mot = mot.capitalize()
                    nom += f"{mot} "
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
            pays = mot.replace("(","").replace(")","")
            spamwriter.writerow([row[0],row[1],row[2],nom,row[4],row[5],row[6],stade,ville,pays,row[8],row[9],row[10],row[11],row[12]])