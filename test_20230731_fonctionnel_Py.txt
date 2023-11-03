# test
"""
  un petit fichier de tests exécutable avec l'invite de commandes (cmd)
   avec la commande >>> py test.py
   ou en saisissant d'abord >>> python
   puis le code ...
   et pour resortir des exécutions python
   >>> exit()
   ou faire Control Z puis Entrée
"""

nom = 'Dumortier'
prenom = "Christophe"
print(f"Bonjour {prenom} { nom }, ça va ?")
print(F"Bonjour {prenom} { nom }, ça va ?")
# affiche Bonjour Christophe Dumortier, ça va ?

"""
la f string (ou F string, les deux fonctionnent avec f ou F) ne fonctionne pas dans le terminal visiblement avec commande python,
par contre cela fonctionne avec py à la place python
"""

print(nom, prenom) 
# affiche Dumortier Christophe







