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

print "test"

nom = 'Dumortier'
prenom = "Christophe"
print(f"Bonjour {prenom} { nom }, ça va ?")
print(F"Bonjour {prenom} { nom }, ça va ?")
# affiche Bonjour Christophe Dumortier, ça va ?

print(f"test d'analyse avec Sonar Cloud")

"""
la f string (ou F string, les deux fonctionnent avec f ou F) ne fonctionne pas dans le terminal visiblement avec commande python,
par contre cela fonctionne avec py à la place python
"""

# exemple fonctionnel de docstring
def my_function(nom, prenom):
  """
     affiche le message Salut avec le nom et le prénom
    Args:
      1er argument : le nom
      2ème argument : le prénom
    Return:
      en sortie : Salut suivi du nom et du prénom passés en arguments 
  """
  print("Salut",nom, prenom) 
  
my_function(nom, prenom)
# affiche Dumortier Christophe

print(my_function.__doc__)

print("*******")

# autre exemple fonctionnel de docstring, mais sur une seule ligne (pour les cas les plus simples)
def my_coucou_function():
  """affiche coucou - ne prend aucun argument et retourne une chaîne de caractères avec le message coucou"""
  print("coucou")

print(my_coucou_function.__doc__)

print("*******")

name=""
# autre exemple de docstring
def search_film(name):
    """Cherche un film selon un nom donné.
 
    Attrs:
    - name (str): le nom utilisé pour la recherche.
 
    Returns:
    - un objet `film` si un film a été trouvé, ou None.
    """
    # ...

