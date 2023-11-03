# le module csv existe nativement dans Python, donc il n'est pas nécessaire de l'installer avec pip install
import csv
# import du package requests et de Beautiful Soup - tous deux installés avec pip install
import pip._vendor.requests
# import bs4.builder._htmlparser - installé avec pip install
from bs4 import BeautifulSoup 

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
# fichier1 = open("fichier_a_lire.txt")
# print(fichier1.read())

# en sortie :
"""
Bonjour Christophe, j'espÃ¨re que tout va bien
Eric est allÃ© au cinÃ©ma
CÃ©dric a manger son sandwich
"""

# lecture du fichier couleurs_preferees.csv ligne par ligne en tenant compte du séparateur virgule (comma)
with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

"""
en sortie, grâce au delimiter - séparateur choisi :
['nom', 'metier', 'couleur_preferee']
['Jacob Smith', 'IngÃ©nieur en informatique', 'Violet']
['Nora Scheffer', 'StratÃ©giste numÃ©rique', 'Bleu']
['Emily Adams', 'Responsable Marketing', 'Orange']
"""
print()

# lecture du fichier couleurs_preferees.csv ligne par ligne en tenant compte du séparateur virgule (comma) même sans l'avoir préciser en params à la méthode reader()
with open('couleurs_preferees.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line," et line[2]:",line[2])
"""
en sortie :
['nom', 'metier', 'couleur_preferee']  et line[2]: couleur_preferee
['Jacob Smith', 'IngÃ©nieur en informatique', 'Violet']  et line[2]: Violet
['Nora Scheffer', 'StratÃ©giste numÃ©rique', 'Bleu']  et line[2]: Bleu
['Emily Adams', 'Responsable Marketing', 'Orange']  et line[2]: Orange
"""
print()

# lecture du fichier couleurs_preferees.csv ligne par ligne en tenant compte de l'en-tête, grâce à DictReader() à la place de reader() et du séparateur virgule (comma) même sans l'avoir préciser en params à la méthode reader()
with open('couleurs_preferees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line," et line['metier']:",line['metier'])
"""
en sortie, on obtient cette fois-ci un Dictionnaire :
{'nom': 'Jacob Smith', 'metier': 'IngÃ©nieur en informatique', 'couleur_preferee': 'Violet'}  et line['metier']: IngÃ©nieur en informatique
{'nom': 'Nora Scheffer', 'metier': 'StratÃ©giste numÃ©rique', 'couleur_preferee': 'Bleu'}  et line['metier']: StratÃ©giste numÃ©rique
{'nom': 'Emily Adams', 'metier': 'Responsable Marketing', 'couleur_preferee': 'Orange'}  et line['metier']: Responsable Marketing
"""
print()

# lecture du fichier couleurs_preferees.csv ligne par ligne en tenant compte du séparateur virgule (comma), avec DictReader (pour la reconnaissance de l'en-tête)
with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])

"""
en sortie, grâce au DictReader (pour la reconnaissance de l'en-tête) et au delimiter - séparateur choisi :
Jacob Smith travaille en tant que IngÃ©nieur en informatique et sa couleur préférée est Violet
Nora Scheffer travaille en tant que StratÃ©giste numÃ©rique et sa couleur préférée est Bleu
Emily Adams travaille en tant que Responsable Marketing et sa couleur préférée est Orange
"""
print()

# lecture du fichier couleurs_preferees_depuis_Open_Office_Excel.csv ligne par ligne en tenant compte du séparateur virgule (comma), avec DictReader (pour la reconnaissance de l'en-tête)
# cette fois-ci je suis parti d'un fichier Open Office Excel, j'ai renseigné les cellules, et je l'ai enrgistré sous format .csv, en acceptant les choix proposés
with open('couleurs_preferees_depuis_Open_Office_Excel.csv') as fichier1_csv:
    reader = csv.DictReader(fichier1_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])

"""
en sortie, grâce au DictReader (pour la reconnaissance de l'en-tête) et au delimiter - séparateur choisi :
Jacob Smith travaille en tant que Ingénieur en informatique et sa couleur préférée est Violet
Nora Schaeffer travaille en tant que Stratégiste numérique et sa couleur préférée est Bleu
Emily Adams travaille en tant que Responsable Marketing et sa couleur préférée est Orange
Christophe Dumortier travaille en tant que Ingénieur en informatique et sa couleur préférée est Vert
"""
print()

"""
pour scrapper le contenu d'une page Web 
à l'aide du module requests 
"""

url = "https://www.gov.uk/"
# on récupère le contenu HTML de ce lien
reponse = pip._vendor.requests.get(url)
page = reponse.content

# on transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
# à présent, avec cette variable soup, je peux récupérer plein d'informations sur cette page HTML

# récupération de tous les titres de liens
# "govuk-link"
# "gem-c-document-list__item-title"
titres = soup.find_all("a", class_="govuk-link")
descriptions = soup.find_all("p", class_="gem-c-layout-super-navigation-header__navigation-second-item-description")

for description in descriptions:
    print("description:",description)

# Créer une liste pour les en-tête
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)

    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for titre, description in zip(titres, descriptions):
        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        ligne = [titre, description]
        writer.writerow(ligne)
"""
en sortie dans le fichier data.csv :
titre,description

"<a class=""govuk-link"" data-module=""gem-track-click"" data-track-action=""Cookie banner settings clicked from confirmation"" data-track-category=""cookieBanner"" href=""/help/cookies"">change your cookie settings</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">Departments, agencies and public bodies</p>"

"<a class=""govuk-link"" data-module=""gem-track-click"" data-track-action=""Cookie banner settings clicked from confirmation"" data-track-category=""cookieBanner"" href=""/help/cookies"">change your cookie settings</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">News stories, speeches, letters and notices</p>"

"<a class=""govuk-link"" href=""/help/cookies"">View cookies</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">Detailed guidance, regulations and rules</p>"

"<a class=""govuk-link gem-c-layout-super-navigation-header__navigation-second-item-link"" data-ga4-link='{""event_name"":""navigation"",""type"":""header menu bar"",""index"":{""index_section"":1,""index_link"":1,""index_section_count"":4},""index_total"":16,""section"":""Topics""}' data-track-action=""topicsLink"" data-track-category=""headerClicked"" data-track-dimension=""Benefits"" data-track-dimension-index=""29"" data-track-label=""/browse/benefits"" href=""/browse/benefits"">Benefits</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">Reports, analysis and official statistics</p>"

"<a class=""govuk-link gem-c-layout-super-navigation-header__navigation-second-item-link"" data-ga4-link='{""event_name"":""navigation"",""type"":""header menu bar"",""index"":{""index_section"":1,""index_link"":2,""index_section_count"":4},""index_total"":16,""section"":""Topics""}' data-track-action=""topicsLink"" data-track-category=""headerClicked"" data-track-dimension=""Births, death, marriages and care"" data-track-dimension-index=""29"" data-track-label=""/browse/births-deaths-marriages"" href=""/browse/births-deaths-marriages"">Births, death, marriages and care</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">Consultations and strategy</p>"

"<a class=""govuk-link gem-c-layout-super-navigation-header__navigation-second-item-link"" data-ga4-link='{""event_name"":""navigation"",""type"":""header menu bar"",""index"":{""index_section"":1,""index_link"":3,""index_section_count"":4},""index_total"":16,""section"":""Topics""}' data-track-action=""topicsLink"" data-track-category=""headerClicked"" data-track-dimension=""Business and self-employed"" data-track-dimension-index=""29"" data-track-label=""/browse/business"" href=""/browse/business"">Business and self-employed</a>","<p class=""gem-c-layout-super-navigation-header__navigation-second-item-description"">Data, Freedom of Information releases and corporate reports</p>"


"""

