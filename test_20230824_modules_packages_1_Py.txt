# import mon_module
# resultat = mon_module.ma_fonction()
# ou bien
# from mon_module import ma_fonction
# resultat = ma_fonction()

# import mon_package.mon_module
# resultat = mon_package.mon_module.ma_fonction()
# ou bien
# from mon_package.mon_module import ma_fonction

import requests

# pour récupérer du contenu HTML
if __name__ == '__main__':
    resultat = requests.get("https://google.fr")
    print(resultat.content)
