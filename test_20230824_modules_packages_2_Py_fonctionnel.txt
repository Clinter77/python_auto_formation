import pip._vendor.requests

# pour récupérer du contenu HTML
if __name__ == '__main__':
    resultat = pip._vendor.requests.get("https://google.fr")
    # print(resultat) # en sortie : <Response [200]>
    print(resultat.content) # content, le contenu
