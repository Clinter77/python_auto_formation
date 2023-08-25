# import du package requests
import pip._vendor.requests

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

page = pip._vendor.requests.get(url)

# Voir le code HTML source de ce Site
print(page.content)

    