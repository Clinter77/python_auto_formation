# import du package requests et de Beautiful Soup
import pip._vendor.requests
# import bs4.builder._htmlparser
from bs4 import BeautifulSoup 

"""
pour scrapper le contenu d'une page Web 
à l'aide du module requests 
"""

# fonctionne aussi ainsi :
# url = "https://google.fr"

# url = "https://www.google.fr"


""" 
# pour récupérer du contenu HTML
if __name__ == '__main__':
    response = pip._vendor.requests.get(url)
    html_code = response.text
    
    # print(resultat) # en sortie : <Response [200]>
    # print(resultat.content) # content, le contenu
    
    print(html_code)
"""

url = "https://www.gov.uk/search/news-and-communications"

# on récupère le contenu HTML de ce lien
# page = pip._vendor.requests.get(url)
reponse = pip._vendor.requests.get(url)
print(reponse,"\n") # en sortie : <Response [200]>
# pour afficher la page HTML
page = reponse.content
# print("page :")
# print(page)
# en sortie : tout le contenu HTML de cette page

# on transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
# à présent, avec cette variable soup, je peux récupérer plein d'informations sur cette page HTML

print("soup.title:",soup.title)
# en sortie : soup.title: <title>News and communications - GOV.UK</title>

# récupération de tous les titres de liens
# avant : class_name = "homepage-most-viewed-list__item" mais en sortie j'obtenais un tableau (une liste) vide
class_name = "govuk-link"
# class_name = "gem-c-document-list__item-title"
titres = soup.find_all("a", class_=class_name)
print("titres:\n",titres)
# en sortie : tous les liens de la page ayant ce class_name

titre_textes = []
# on itère afin d'ajouter chaque élément à la liste créée (au tableau)
for titre in titres:
    # on ajoute à notre liste avec la méthode append()
	titre_textes.append(titre.string)
    # titre.string - string car c'est une propriété HTML qu'on récupère

# affichage
for titre in titre_textes:
    print("titre:\n\t",titre)
# en sortie, l'affichage des titres des liens est plus lisible :
""" 
titre:
         change your cookie settings
titre:
         change your cookie settings
titre:
         View cookies
titre:
         Benefits
titre:
         Births, death, marriages and care
titre:
         Business and self-employed
etc ...
"""

# récupération de toutes les descriptions
descriptions = soup.find_all("p", "gem-c-document-list__item-description")
print("descriptions:\n",descriptions)
# en sortie : tous les éléments de balises <p> ayant cette classe (passée en deuxième argument)

description_textes = []
# on itère afin d'ajouter chaque élément à la liste créée (au tableau)
for description in descriptions:
    # on ajoute à notre liste avec la méthode append()
	description_textes.append(description.string)
    # description.string - string car c'est une propriété HTML qu'on récupère

# affichage
for description in description_textes:
    print("description:\n\t",description)
# en sortie l'affichage des descriptions est plus lisible :
""" 
description:
         The Fish Health Inspectorate (FHI) have found Koi herpesvirus (KHV) disease in fish at the following sites in England and Wales
description:
         A letter sent from Sarah Cardell, CEO of the Competition and Markets Authority, to the Secretary of State for Levelling Up, Housing and Communities on the CMA's work in the housing sector.
description:
         A new consultation, launched today, will advise unions on reasonable steps they should take to ensure minimum service levels are achieved during strike action.
description:
         Anniversary ...
etc ...
"""

# *************

# Voir le code HTML source de ce Site
# print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')
# à présent, avec cette variable soup, je peux récupérer plein d'informations sur cette page HTML

# Récupération du titre de la page HTML
# print("soup.title:",soup.title)
# en sortie : soup.title: <title>News and communications - GOV.UK</title>

# Récupération de la chaîne de caractères du titre HTML
# print("soup.title.string:",soup.title.string)
# en sortie : soup.title.string: News and communications - GOV.UK

# Trouver tous les éléments avec la balise <a>
# print("soup.find_all('a'):",soup.find_all('a'))
""" 
en sortie :
soup.find_all('a'): [<a class="gem-c-skip-link govuk-skip-link govuk-!-display-none-print" data-module="govuk-skip-link" href="#content">Skip to main content</a>, <a class="govuk-link" data-module="gem-track-click" data-track-action="Cookie banner settings clicked from confirmation" data-track-category="cookieBanner" href="/help/cookies">change your cookie settings</a>, <a class="govuk-link" data-module="gem-track-click" data-track-action="Cookie banner settings clicked from confirmation" data-track-category="cookieBanner" href="/help/cookies">change your cookie settings</a>, <a class="govuk-link" href="/help/cookies">View cookies</a>, <a class="govuk-header__link govuk-header__link--homepage" data-ga4-link='{"event_name":"navigation","type":"header menu bar","external":"false","text":"GOV.UK","section":"Logo","index":{"index_link":1,"index_section":0,"index_section_count":2},"index_total":1}' data-track-action="logoLink" data-track-category="headerClicked" data-track-dimension="GOV.UK" data-track-dimension-index="29" data-track-label="https://www.gov.uk" href="https://www.gov.uk" id="logo" title="Go to the GOV.UK homepage">
<span class="govuk-header__logotype"> ... etc ... avec la suite ...
"""

# Trouver tous les éléments avec id
# print("soup.find('id'):",soup.find('id'))
# en sortie : soup.find('id'): None

# Trouver les éléments avec l’id du «  »
# print("soup.find_all('a'):",soup.find(id=""))