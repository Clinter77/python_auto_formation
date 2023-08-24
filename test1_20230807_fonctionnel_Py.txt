# test1
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
print(f"Bonjour {prenom} { nom }, ça va ? ", end="") # l'ajout de , end="" fera qu'il n'y aura pas de retour à la ligne entre les deux messages affichés, ils seront surla même ligne
print(F"Bonjour {prenom} { nom }, ça va ?")
# affiche Bonjour Christophe Dumortier, ça va ? Bonjour Christophe Dumortier, ça va ?

"""
la f string (ou F string, les deux fonctionnent avec f ou F) ne fonctionne pas dans le terminal visiblement avec commande python,
par contre cela fonctionne avec py à la place python
"""

print(nom,prenom, ", 45 ans") 
# affiche Dumortier Christophe , 45 ans

"""
print(nom,prenom, ", 45 ans") ou print(nom, prenom, ", 45 ans") renvoient tous les deux Dumortier Christophe , 45 ans (avec l'espace entre mon nom et mon prénom)
l'espace entre nom et prénom n'a aucune incidence, ils seront de toute façon séparé par un espace, par contre entre les guillemets simples ou doubles, à moi d'y penser
"""

print(12 + 2 * 5) # renvoie 22, il a bien appliqué la priorité de la multiplication sur l'addition
print(2 * 5 + 12) # renvoie 22, il a bien appliqué la priorité de la multiplication sur l'addition

temps_ensoleille = True
temps_ensoleille = False

print("-------------")

print(temps_ensoleille) # renvoie False

print("-------------")

personnages = ["Tintin", "Haddock", "Triffon Tournesol"]
print(personnages[0]) # affichera Tintin
print(personnages[2]) # affichera Triffon Tournesol
print("-------------")
langage_de_programmation = "PYTHON"

print("langage_de_programmation[1]: ", langage_de_programmation[1], "!")
# affichera langage_de_programmation[1]: Y !

print("langage_de_programmation[1] : "+langage_de_programmation[1]+" !")
# affichera langage_de_programmation[1] : Y !

print("-------------")

personnages.append("Hergé")
print(personnages) # affiche le contenu de la liste : ['Tintin', 'Haddock', 'Triffon Tournesol', 'Hergé']
print(len(personnages)) # renvoie 4

personnages.remove("Triffon Tournesol")
print(personnages) # affiche ['Tintin', 'Haddock', 'Hergé']

# remove()  retire uniquement la première instance du terme que vous saisissez.

personnages.pop(2) # supprime le contenu de la liste ayant l'index 2, donc le troisième élément
print(personnages) # affiche ['Tintin', 'Haddock']

personnages.pop() # supprime le dernier élément car aucun index n'est fourni
print(personnages) # affiche ['Tintin']
print("longueur de la liste maintenant",len(personnages)) # affiche longueur de la liste maintenant 1

personnages.append("Haddock")
personnages.append("Triffon Tournesol")
print("longueur de la liste maintenant",len(personnages)) # affiche longueur de la liste maintenant 3
print(personnages) # affiche ['Tintin', 'Haddock', 'Triffon Tournesol']
personnages[2]="Triffon" # pour modifier, remplacer le 2ème élémnet par Triffon au lieu de Triffon Tournesol
print("la liste après modification :")
print(personnages) # affiche ['Tintin', 'Haddock', 'Triffon']

personnages.sort()
print("la liste triée",personnages) # affiche la liste triée par ordre croissant alphabétique - affiche : la liste triée ['Haddock', 'Tintin', 'Triffon']

personnages.reverse()
print("la liste triée par ordre inversé ",personnages) # affiche la liste triée par ordre décroissant alphabétique - affiche : la liste triée par ordre inversé  ['Triffon', 'Tintin', 'Haddock']
# avec la concaténation avec ""+ cela n'aurait pas fonctionné, et renvoyé une erreur car il n'y a pas de concaténation possible entre un String et une liste

print("les tuples")
personnages_tuples_immuables = ("Tintin", "Haddock", "Triffon Tournesol")
print(personnages_tuples_immuables)
# personnages_tuples_immuables[2]="Triffon" # renverra une erreur car un tuple est une liste immuable, non modifiable

print("-------------")
print('Tintin' in personnages) # renvoie True, car il est bien présent dans la liste "personnages"
print("Tintin" in personnages) # renvoie True, car il est bien présent dans la liste "personnages"
print("Christophe" in personnages) # renvoie False, car il n'est pas présent dans la liste "personnages"
print("-------------")
print('Haddock' in personnages_tuples_immuables) # renvoie True, car il est bien présent dans le tuple "personnages_tuples_immuables"
print("Christophe" in personnages_tuples_immuables) # renvoie False, car il n'est pas présent dans le tuple "personnages_tuples_immuables"

print("-------------")
print("les dictionnaires en Python")
maVoitureActuelle = {
   "marque": "Opel",
   "annee": 2011,
   "modele": "Corsa 4"
}
print(maVoitureActuelle) # affiche {'marque': 'Opel', 'annee': 2011, 'modele': 'Corsa 4'}
print("sa marque : "+maVoitureActuelle['marque']) # affiche sa marque : Opel
print("sa marque :",maVoitureActuelle['marque']) # affiche sa marque : Opel
print("ajout de la clé 'proprietaire' et de sa valeur 'Christophe' au dictionnaires")
maVoitureActuelle["proprietaire"]="Christophe"
print(maVoitureActuelle) # affiche {'marque': 'Opel', 'annee': 2011, 'modele': 'Corsa 4', 'proprietaire': 'Christophe'}
print("son propriétaire",maVoitureActuelle['proprietaire']) # affiche son propriétaire Christophe

print("modifier la valeur d'une clé du dictionnaire")
maVoitureActuelle["proprietaire"]='Christophe Dumortier'
print("maVoitureActuelle['proprietaire'] : "+maVoitureActuelle['proprietaire']) # affiche maVoitureActuelle['proprietaire'] : Christophe Dumortier

print("Supprimer une paire clé-valeur avec del, suppression de la clé annee")
del maVoitureActuelle["annee"]
print(maVoitureActuelle) # affiche {'marque': 'Opel', 'modele': 'Corsa 4', 'proprietaire': 'Christophe Dumortier'}
print("Supprimer la dernière paire clé-valeur avec popitem(), qui ne prend pas d'argument")
maVoitureActuelle.popitem() # supprime la dernière clé (et sa valeur) du dictionnaire
print(maVoitureActuelle) # affiche {'marque': 'Opel', 'modele': 'Corsa 4'}

print("ré-ajout de la clé 'proprietaire' et de sa valeur 'Christophe' au dictionnaires")
maVoitureActuelle["proprietaire"]="Christophe"
print(maVoitureActuelle) # affiche {'marque': 'Opel', 'modele': 'Corsa 4', 'proprietaire': 'Christophe'}

print(maVoitureActuelle.keys()) # pour afficher les clés de ce dictionnaire : dict_keys(['marque', 'modele', 'proprietaire'])
print(maVoitureActuelle.values()) # pour afficher les valeurs de ce dictionnaire : dict_values(['Opel', 'Corsa 4', 'Christophe'])
print(maVoitureActuelle.items()) # pour afficher les paires clés-valeurs du dictionnaire : dict_items([('marque', 'Opel'), ('modele', 'Corsa 4'), ('proprietaire', 'Christophe')])

print("vérification de l'existence d'une clé dans le dictionnaire demandé")
print("vérification de l'existence de la clé 'proprietaire'")
print("proprietaire" in maVoitureActuelle) # renvoie True, car cette clé est bel et bien présente dans le dictionnaire cité
print("vérification de l'existence de la clé 'annee'")
print('annee' in maVoitureActuelle) # renvoie False, car cette clé n'est pas présente

print("-------------")

class Livre:
  def __init__(self, nom, auteur, nb_pages):
    self.nom = nom
    self.auteur = auteur
    self.nb_pages = nb_pages


nouveau_livre = Livre("Les meilleures pratiques en matière de programmation","Christophe Ferdinand", 500)

print('nouveau livre créé')
print("son nom :",nouveau_livre.nom,", son auteur",nouveau_livre.auteur, ", son nombre de pages",nouveau_livre.nb_pages)

print("modification de l'un de ses attributs")
nouveau_livre.nom="La programmation de A à Z"
print("son nom après modification :",nouveau_livre.nom)

# en sortie :
"""
nouveau livre créé
son nom : Les meilleures pratiques en matière de programmation , son auteur Christophe Ferdinand , son nombre de pages 500
modification de l'un de ses attributs
son nom après modification : La programmation de A à Z
"""

print("-------------")







