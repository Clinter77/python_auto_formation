import csv

# créé un nouveau fichier avec Python, et y placer du contenu - exemple fonctionnel
# création du fichier cité en 1er param, et en 2ème param w pour write (écrire-remplacer-écraser)
# les options du 2ème param sont : r pour read (lire), w pour write (écrire, écraser si fichier avec même nom déjà présent), a pour continuer d'écrire (ça rajoute à l'intérieur, a comme append()), et r+ pour lire et écrire (sans écraser)  
fichier = open("BonjourChristopheNouveauFichier.txt", "w")

# je place le contenu que je veux dans ce nouveau fichier qui sera généré
fichier.write("Bonjour Christophe :)")

# puis je ferme le fichier
fichier.close

# je n'ai plus qu'à consulter le fichier que j'ai généré, et son contenu pour en voir le résultat,
# après avoir bien sûr exécuté de fichier Python en ligne de commande, CMD : 
# py BonjourChristophe.py

# *************

# lecture du fichier BonjourChristopheNouveauFichier.txt
# le fichier d’entrée va être affiché ligne par ligne - comme aucun mode n'a été défini en 2ème param à la méthode open(), c'est le mode par défaut qui sera utilisé, c'est à dire l'option r par défaut pour read (lire)
with open("BonjourChristopheNouveauFichier.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)

print()

# lecture du fichier fichier_a_lire.txt
fichier1 = open("fichier_a_lire.txt")
print(fichier1.read())

# en sortie :
"""
Bonjour Christophe, j'espÃ¨re que tout va bien
Eric est allÃ© au cinÃ©ma
CÃ©dric a manger son sandwich
"""

# lecture du fichier fichier_a_lire.txt
with open("fichier_a_lire.txt") as fichier2:
    for ligne in fichier2:
        # faire quelque chose avec une ligne
        print(ligne)
# en sortie :
"""
Bonjour Christophe, j'espÃ¨re que tout va bien

Eric est allÃ© au cinÃ©ma

CÃ©dric a manger son sandwich
"""
