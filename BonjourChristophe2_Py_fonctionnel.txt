# le module csv existe nativement dans Python, donc il n'est pas nécessaire de l'installer avec pip install
import csv
# import du package requests et de Beautiful Soup - tous deux installés avec pip install
import pip._vendor.requests
# import bs4.builder._htmlparser - installé avec pip install
from bs4 import BeautifulSoup 

# tutoriel Openclassrooms
print('tuto')

url1 = "https://www.gov.uk/search/news-and-communications"
reponse1 = pip._vendor.requests.get(url1)
page1 = reponse1.content

soup1 = BeautifulSoup(page1, "html.parser")

titres1 = soup1.find_all("a", class_="gem-c-layout-super-navigation-header__navigation-second-item-link")
titre1_textes = []
for titre in titres1:
    titre1_textes.append(titre.string)

descriptions1 = soup1.find_all("p", class_="gem-c-layout-super-navigation-header__navigation-second-item-description")
description1_textes = []
for description in descriptions1:
    description1_textes.append(description.string)

print()

print("liens :")
for t in titre1_textes:
    print(t)
"""
en sortie :
liens :
Benefits
Births, death, marriages and care
Business and self-employed
Childcare and parenting
Citizenship and living in the UK
Crime, justice and the law
Disabled people
Driving and transport
Education and learning
Employing people
Environment and countryside
Housing and local services
Money and tax
Passports, travel and living abroad
Visas and immigration
Working, jobs and pensions
Departments
News
Guidance and regulation
Research and statistics
Policy papers and consultations
Transparency
"""

print()   

print("descriptions :")
for d in description1_textes:
    print(d)
"""
en sortie :
descriptions :
Departments, agencies and public bodies
News stories, speeches, letters and notices
Detailed guidance, regulations and rules
Reports, analysis and official statistics
Consultations and strategy
Data, Freedom of Information releases and corporate reports
"""

# écriture des résulats récupérés dans un fichier.csv

en_tete = ['titre','description']

with open('data1.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete) # écriture de l'en-tête
    for titre, description in zip(titre1_textes, description1_textes): # zip() pour pouvoir travailler sur les deux, les titres et les descriptions
        writer.writerow([titre, description])
