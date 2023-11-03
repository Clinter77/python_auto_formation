# test3

# from email.policy import default
import datetime
import sys

print("test3.py")
"""
   un petit fichier de tests exécutable avec l'invite de commandes (cmd)
   avec la commande >>> py test.py
   ou en saisissant d'abord >>> python
   puis le code ...
   et pour resortir des exécutions python
   exit()
   ou faire Control Z puis Entrée
"""

date = str(datetime.datetime.now())
print("date :",date)
print("Version :",sys.version)

print("---------------------------------------------------------")

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

personnages.append("Hergé") # ajoute Hergé à la liste des personnages (au tableau), grâce à append()
print(personnages) # affiche le contenu de la liste : ['Tintin', 'Haddock', 'Triffon Tournesol', 'Hergé']
print(len(personnages)) # renvoie 4

# modifier un personnage dans la liste (via l'index fourni en params) :
# personnages[0]="TINTIN"
# il suffit de ré-affecter une autre valeur à un indice donné

personnages.remove("Triffon Tournesol") # supprime le personnage Triffon Tournesol de la liste, avec la méthode remove()
print(personnages) # affiche ['Tintin', 'Haddock', 'Hergé']

# remove()  retire uniquement la première instance du terme que vous saisissez.

personnages.pop(2) # la méthode pop() supprime le contenu de la liste ayant l'index 2, donc le troisième élément
print(personnages) # affiche ['Tintin', 'Haddock']

personnages.pop() # la méthode supprimera alors le dernier élément car aucun index n'est fourni
print(personnages) # affiche ['Tintin']
print("longueur de la liste maintenant",len(personnages)) # affiche longueur de la liste maintenant 1

personnages.append("Haddock") # ajout du personnage Haddock à la liste (au tableau)
personnages.append("Triffon Tournesol")
print("longueur de la liste maintenant",len(personnages)) # affiche longueur de la liste maintenant 3
print(personnages) # affiche ['Tintin', 'Haddock', 'Triffon Tournesol']
personnages[2]="Triffon" # pour modifier, remplacer le 2ème élémnet par Triffon au lieu de Triffon Tournesol
print("la liste après modification :")
print(personnages) # affiche ['Tintin', 'Haddock', 'Triffon']

# méthode sort() pour trier la liste dans le sens croissant
personnages.sort()
print("la liste triée",personnages) # affiche la liste triée par ordre croissant alphabétique - affiche : la liste triée ['Haddock', 'Tintin', 'Triffon']

# méthode reverse() pour trier la liste dans le sens décroissant
personnages.reverse()
print("la liste triée par ordre inversé ",personnages) # affiche la liste triée par ordre décroissant alphabétique - affiche : la liste triée par ordre inversé  ['Triffon', 'Tintin', 'Haddock']
# avec la concaténation avec ""+ cela n'aurait pas fonctionné, et renvoyé une erreur car il n'y a pas de concaténation possible entre un String et une liste

print("les tuples")
personnages_tuples_immuables = ("Tintin", "Haddock", "Triffon Tournesol")
print(personnages_tuples_immuables)
# personnages_tuples_immuables[2]="Triffon" # renverra une erreur car un tuple est une liste immuable, non modifiable

print("-------------")
# équivalents à contains() et includes() : in
# chercher la présence d'un contenu string dans la liste (dans le tableau) - avec in :
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

# les Classes :
class Livre:
  # constructeur de la Classe, méthode __init__(self, param1, param2, ...):
  def __init__(self, nom, auteur, nb_pages):
    self.nom = nom
    self.auteur = auteur
    self.nb_pages = nb_pages

# instanciation d'un nouveau livre
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
print("09 août 2023 - 09/08/2023")

# utilisation de liste, de boucles (de loop) for in (for element_of_liste in liste:), for in range with index (for i in range(len(ma_liste)):), et de boucle while (while i < len(liste):) 

liste_mes_amis_Afpa = ["Cédric", "Eric", "Jean-Seb", "Seb"]
print("liste_mes_amis_Afpa :",liste_mes_amis_Afpa) # en sortie : liste_mes_amis_Afpa : ['Cédric', 'Eric', 'Jean-Seb', 'Seb']
print("celui qui se trouve à l'indice 0 - liste_mes_amis_Afpa[0] :", liste_mes_amis_Afpa[0]) # en sortie : celui qui se trouve à l'indice 0 - liste_mes_amis_Afpa[0] : Cédric
ami_cedric = liste_mes_amis_Afpa[0]
for caractere in ami_cedric:
  print(caractere)
# print("\n") # permet d'aller à la ligne aussi - rajoute une entrée
# en sortie :
"""
C
é
d
r
i
c

"""
i=0
print("longueur, len(ami_cedric) :",len(ami_cedric))
while i < len(ami_cedric):
  print("i",i,ami_cedric[i])
  i+=1

i=0
print('*******')
# en sortie :
"""
i 0 C
i 1 é
i 2 d
i 3 r
i 4 i
i 5 c
""" 
for i in range(len(ami_cedric)):
  print("i",i,ami_cedric[i])
# en sortie :
"""
i 0 C
i 1 é
i 2 d
i 3 r
i 4 i
i 5 c
"""
print('*******')

for ami in liste_mes_amis_Afpa:
  print("ami",ami)
print("nb amis",len(liste_mes_amis_Afpa))
print('*******')
# en sortie :
"""
ami Cédric
ami Eric
ami Jean-Seb
ami Seb
nb amis 4
""" 

# print("liste_mes_amis_Afpa : "+liste_mes_amis_Afpa) lève une Exception
"""
TypeError: can only concatenate str (not "list") to str
"""

temps_ensoleille = True
print("temps_ensoleille = True - type(temps_ensoleille)",type(temps_ensoleille),"et sa valeur",temps_ensoleille)
# renvoie : temps_ensoleille = True - type(temps_ensoleille) <class 'bool'> et sa valeur True

variable = 123
print("variable = 123 - type(variable)",type(variable),"et sa valeur",variable)
# renvoie : variable = 123 - type(variable) <class 'int'> et sa valeur 123

variable = str(variable)
print("variable = str(variable) - type(variable)",type(variable),"et sa valeur",variable)
# renvoie : variable = str(variable) - type(variable) <class 'str'> et sa valeur 123

variable = 123.45
print("variable = 123.45 - type(variable)",type(variable),"et sa valeur",variable)
# renvoie : variable = 123.45 - type(variable) <class 'float'> et sa valeur 123.45

variable=int(variable)
print("variable=int(variable) - type(variable)",type(variable),"et sa valeur",variable)
# renvoie : variable=int(variable) - type(variable) <class 'int'> et sa valeur 123
# (il a bien récupéré la partie entière de la variable

"""
exemples possibles de cast :
int(variable)
float(variable)
str(variable) -> Cast en string
"""



# les conditions (bloc if/else, if/elif/else, et équivalent switch cases (les match cases) :

if type(variable)==int:
  print("variable est en Integer")
else :
  print("variable est d'un autre type qu'Integer") 
# en sortie : variable est en Integer

variable = float(variable)

if type(variable)==int :
  print("variable est en Integer",'et sa valeur est de',variable)
elif type(variable)==float:
  print("variable est en Float",'et sa valeur est de',variable)
else :
  print("variable n'est ni de type Integer ni de type float") 
# en sortie : variable est en Float et sa valeur est de 123.0

print("-------------")

variable += 0.123456789
print('après avoir lui avoir ajouté quelques chiffres après la virgule - variable += 0.123456789')
if type(variable)==int :
  print("variable est en Integer",'et sa valeur est de',variable)
elif type(variable)==float:
  print("variable est en Float",'et sa valeur est de',variable)
else :
  print("variable n'est ni de type Integer ni de type float") 
# en sortie : variable est en Float et sa valeur est de 123.123456789

print("en type Float") if type(variable)==float else print('autre type que Float')
# en sortie : en type Float

print("-------------")

variable-=0.000006789
print('après avoir lui avoir enlevé quelques chiffres après la virgule - variable-=0.000006789')
print("type(variable)",type(variable),"et sa valeur",variable)
# en sortie : type(variable) <class 'float'> et sa valeur 123.12345

print("-------------")

a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement

print("-------------")

print("Switch case statement equivalent - match case - tous les cas fontionnent, y compris le default case _")

jour="lundi"
result=""

def check_day_of_week(jour):
  print("jour",jour)
  match jour:
    case 'lundi':
      print('cas lundi')
      result="Le Lundi au Soleil"
      return result
    case 'mardi':
      print('cas mardi')
      result="Moordi gras"
      return result
    case 'mercredi':
      print('cas mercredi')
      result="Mer creux dit"
      return result
    case 'jeudi':
      print('cas jeudi')
      result="Je dis Jeudi"
      return result
    case 'vendredi':
      print('cas vendredi')
      result="Vendredi tout est permis, y compris les blagues"
      return result
    case 'samedi':
      print('cas samedi')
      result="ça me dit ..."
      return result
    case 'dimanche':
      print('cas dimanche')
      result="Retroussons-nous les manches !"
      return result
    case _:
      print('cas inconnu')
      result="jour inconnu au bataillon"
      return result

result = check_day_of_week(jour) # si je n'avais pas placé le résultat de l'appel de la méthode check_day_of_week() dans result ainsi, result serais vide à l'affichage après
print("result :",result) # affichera : result : Le Lundi au Soleil
print("result :\t",result) # affichera : result :         Le Lundi au Soleil (la tabulation a été ajoutée grâce au \t)

print("result :\n",result)
"""
affichera :
result :
 Le Lundi au Soleil
"""

print()

# Classes and Objects

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
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

print("-------------")
print("10 août 2023 - 10/08/2023")

variable_de_test = 'coucou'
# if (type(variable_de_test) == int): print("c'est un entier") # fonctionnel

# avant la version 3.10 qui a vu l'apparition des match cases - tous les cas fonctionnent :
if type(variable_de_test)==int:
  print("cas int - variable_de_test est de type integer")
elif type(variable_de_test)==float:
  print("cas float - variable_de_test est de type float")
elif type(variable_de_test)==bool:
  print("cas bool - variable_de_test est de type boolean")
elif (type(variable_de_test)==str):
  print("cas str - variable_de_test est de type string")
else:
  print("cas avec type inconnu")

# en sortie : dans le cas présent : cas str - variable_de_test est de type string

# liste d'entiers avec une recherche de présence de l'élément dans le tableau (la liste) :
array_of_test={1,2,3,4,5,6,7.7,8.8,9,10,20,30,40,50,"coucou"}
for element in array_of_test:
  print(element)

number_input="coucou"

if number_input in array_of_test:
  print("le paramètre rentré \"",number_input, "\" est bien présent dans la liste")
else:
  print(f"le paramètre rentré \'{number_input}\' n'est pas présent dans la liste")

# en sortie :
# avec en entrée 7, affiche : le nombre rentré " 7 " est bien présent dans la liste
# avec en entrée 42, affiche : le nombre rentré '42' n'est pas présent dans la liste

# pareil, cette fois-ci avec des tuples :
invites_dont_le_prenom_ne_change_pas = ("Capitaine Christophe","Lieutenant Alan", 'Bobes', "Carlo", 'Karlitos', "Tchang", "Ventopuces", 'Sven', "Tzvain")

invite_cherche = "Capitaine Christophe"

if (invite_cherche in invites_dont_le_prenom_ne_change_pas): 
  print("L'invité '"+invite_cherche+"' est présent")
else:
  print(F"L'invité {invite_cherche} est absent")

# en sortie :
"""
  avec en entrée invite_cherche = "Christophe", en sortie : L'invité Christophe est absent
  avec en entrée invite_cherche = "Capitaine Christophe", en sortie : L'invité 'Capitaine Christophe' est présent
  avec en entrée invite_cherche = "Bob", en sortie : L'invité Bob est absent
  avec en entrée invite_cherche = "bobes", en sortie : L'invité bobes est absent
  avec en entrée invite_cherche = "Bobes", en sortie : L'invité 'Bobes' est présent
  Comme on peut le constater, c'est sensible à la casse, et il faut que toute la chaîne soit présente, et pas seulement en partie
"""

dictionnaire_premier_livre = {
  "nom":"Les oiseaux s'envolent toujours plus loin",
  "auteur":"Christian Koulnitch"
}

print(dictionnaire_premier_livre) # en sortie : {'nom': "Les oiseaux s'envolent toujours plus loin", 'auteur': 'Christian Koulnitch'}
print(dictionnaire_premier_livre['nom']) # en sorite : Les oiseaux s'envolent toujours plus loin
print(dictionnaire_premier_livre["auteur"]) # en sortie : Christian Koulnitch

# vérification et recherche d'une clé dans le dictionnaire - option 1 - fonctionnel :
if ("auteur" in dictionnaire_premier_livre):
  print("la clé ''auteur'' est présente dans dictionnaire_premier_livre")
else:
  print("La clé ''auteur'', est absente des clés du dictionnaire_premier_livre")
# en sortie :
# avec en entrée : la clé ''auteur'' est présente dans dictionnaire_premier_livre

print('*******')

# vérification et recherche d'une clé dans le dictionnaire - option 2 - fonctionnel :
key_to_search="annee"
if (key_to_search in dictionnaire_premier_livre.keys()):
  print(f"la clé ''{key_to_search}'' est présente dans dictionnaire_premier_livre")
else:
  print(f"La clé cherchée ''{key_to_search}'', est absente des clés de dictionnaire_premier_livre")
# en sortie :
"""
  avec en entrée "auteur" : la clé ''auteur'' est présente dans dictionnaire_premier_livre
  avec en entrée "annee" : La clé cherchée ''annee'', est absente des clés de dictionnaire_premier_livre
"""
print('*******')
# vérification et recherche d'une valeur dans le dictionnaire - fonctionnel :
value_to_search="Les oiseaux s'envolent toujours plus loin"
if (value_to_search in dictionnaire_premier_livre.values()):
  print(f"la valeur ''{value_to_search}'' est présente dans dictionnaire_premier_livre")
else:
  print(f"La valeur cherchée ''{value_to_search}'', est absente du dictionnaire_premier_livre")
# en sortie :
"""
  avec en entrée "Christian Koulnitch" : la valeur ''Christian Koulnitch'' est présente dans dictionnaire_premier_livre
  avec en entrée "Christian" : La valeur cherchée ''Christian'', est absente du dictionnaire_premier_livre
  avec en entrée "oiseaux" : La valeur cherchée ''oiseaux'', est absente du dictionnaire_premier_livre
  avec en entrée "les oiseaux s'envolent toujours plus loin" : La valeur cherchée ''les oiseaux s'envolent toujours plus loin'', est absente du dictionnaire_premier_livre
  avec en entrée "Les oiseaux s'envolent toujours plus loin" : la valeur ''Les oiseaux s'envolent toujours plus loin'' est présente dans dictionnaire_premier_livre
"""

# inversion de l'ordre de listes avec méthodes personnelle et utilisation de reverse() - fonctionnels

chaine = "Aujourd'hui il fait chaud !"

print("chaine :")
print(chaine) # en sortie : Aujourd'hui il fait chaud !

def reverse_the_string(s):
    str = ""
    for i in s:
        str = i + str # ajoute i à gauche du caractère existant actuel dans str par concaténation, donc inverse la chaîne
        # print(str) - ça fait joli en plus d'être pratique pour la compréhension
    return str
 
s = chaine
 
print("La chaîne au début : ", end="")
print(s)
# en sortie : La chaîne au début : Aujourd'hui il fait chaud !
 
print("La chaîne inversée, en utilisant une méthode personnalisée : ", end="")
print(reverse_the_string(s))
# en sortie : La chaîne inversée : ! duahc tiaf li iuh'druojuA

print()
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("digits, une liste d'entiers dans l'ordre d'origine :",digits)
digits.reverse()
print("digits, la liste d'entiers inversée, après avoir utilisé la méthode reverse() : ",digits)
# en sortie : La chaîne inversée, en utilisant la méthode reverse() :  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("digits :",digits)
print()
list_of_strings = ["Zozor","Trent","Robert","David","Charlie","Bob","Alan"]
print("list_of_strings, une liste de strings dans l'ordre d'origine :",list_of_strings)
list_of_strings.reverse()
print("list_of_strings, la liste de strings inversée, après avoir utilisé la méthode reverse() : ",list_of_strings)
# en sortie : 
print("list_of_strings : "+str(list_of_strings)) # j'ai ici Castée la liste en string (avec la méthode str()) afin de pouvoir la concaténer avec l'opérateur + dans le print()

print()

list_of_strings2 = ["Zozor","Trent","Robert","David","Charlie","Bob","Alan"]
print("list_of_strings2 :",list_of_strings2)
list_of_strings2.reverse() # la liste est modifiée, inversée
list_of_strings2_reversed = list_of_strings2 # la liste inversée est affectée à une nouvelle liste
print('list_of_strings2_reversed : ',list_of_strings2_reversed) # cette nouvelle liste, qui a reçu la list inversée, est affichée
list_of_strings2.reverse() # remise à l'état d'origine de la liste d'origine
print('list_of_strings2 : ',list_of_strings2) # et réaffichage de celle-ci

"""
en sortie :
  list_of_strings2 : ['Zozor', 'Trent', 'Robert', 'David', 'Charlie', 'Bob', 'Alan']
  list_of_strings2_reversed :  ['Alan', 'Bob', 'Charlie', 'David', 'Robert', 'Trent', 'Zozor']
  list_of_strings2 :  ['Zozor', 'Trent', 'Robert', 'David', 'Charlie', 'Bob', 'Alan']
"""

print()

# tri avec sort() method fonctionnels, mais ne pas afficher directement print(ma_liste.sort()) cela retournerait None
# il faut effectuer le tri dans un premier temps : ma_liste.sort() et ensuite affiché la liste triée-modifiée : print(ma_liste)

# tableau_liste = [45,5,155,35,75,25,15]
# tableau_liste = [45.3, 5.5, 5.2, 5.3, 35.7, 35.1, 75.75, 25.25, 25, 15.0]
tableau_liste = ["Oiseaux","Hiboux","Chats","Ours","Dauphins","Tigres","Jaguars"]

print("voici le tableau_liste avant le tri : ", end="") # pour que cela affiche le tableau_liste sur la même ligne
print(tableau_liste)

# tri du tableau dans un premier temps (ce qui modifie alors le tableau lui-même) :
tableau_liste.sort()

print("voici le tableau_liste trié par ordre croissant : ", end="") # pour que cela affiche le tableau_liste sur la même ligne
print("line 558 - tableau_liste",tableau_liste)

"""
  avec en entrée : tableau_liste = [45,5,155,35,75,25,15] en sortie : 
    non trié : [45, 5, 155, 35, 75, 25, 15]
    trié : [5, 15, 25, 35, 45, 75, 155]
  avec en entrée : tableau_liste = [45.3, 5.5, 5.2, 5.3, 35.7, 35.1, 75.75, 25.25, 25, 15.0] en sortie : 
    non trié : [45.3, 5.5, 5.2, 5.3, 35.7, 35.1, 75.75, 25.25, 25, 15.0]
    trié : [5.2, 5.3, 5.5, 15.0, 25, 25.25, 35.1, 35.7, 45.3, 75.75]
  avec en entrée : tableau_liste = [45,5,155,35,75,25,15] en sortie :
  non trié : ['Oiseaux', 'Hiboux', 'Chats', 'Ours', 'Dauphins', 'Tigres', 'Jaguars']
  trié : ['Chats', 'Dauphins', 'Hiboux', 'Jaguars', 'Oiseaux', 'Ours', 'Tigres']
"""

# fonctionnels - y compris le set (équivalent au HashSet)
tableau_liste.append("Chats") # pour ajouter un élément "Chats"
print("line 574 - tableau_liste",tableau_liste)
# count() est une méthode qui permet de compter le nombre d'occurences du paramètre fourni via sa méthode : liste_matrice_de_recherche.count("element_cherche")
nb_elements_chats_tableau_list = tableau_liste.count("Chats")
print("longueur tableau_liste avant utilisation du Set() ",len(tableau_liste)) # 8
print("nb éléments ''chats'' dans tableau_liste :",nb_elements_chats_tableau_list)

tableau_liste_sorted = sorted(tableau_liste) # tri puis affectation à tableau_liste_sorted
print("line 583",tableau_liste_sorted)
tableau_liste_uniques_elements_sorted = sorted(set(tableau_liste_sorted)) # pour ôter les doublons puis ré-affectation à tableau_liste_uniques_elements

print("tableau_liste_uniques_elements_sorted après utilisation de set() : ",tableau_liste_uniques_elements_sorted)
# en sortie : tableau_liste_uniques_elements_sorted après utilisation de set() :  ['Chats', 'Dauphins', 'Hiboux', 'Jaguars', 'Oiseaux', 'Ours', 'Tigres']

print("longueur du tableau_liste après utilisation du Set() ",len(tableau_liste_uniques_elements_sorted)) # en sortie : 7


# ******************************************************

# inversion de caractères sur une chaîne, et aussi retrait des espaces blanc pour la nouvelle chaîne inversée - fonctionnel
string_to_test = "Coucou"

# fonctionnels
print("string_to_test :",string_to_test)
print("string_to_test.upper() :",string_to_test.upper())
print("string_to_test.lower() :",string_to_test.lower())

# sans global, j'obtiendrai l'erreur : UnboundLocalError: local variable 'string_reversed' referenced before assignment
# string_reversed ça ne fonctionne pas non plus y compris avec le mot clé global


string_reversed = ""

def function_to_reverse_string(string_to_reverse):
  # print("string_to_reverse in my_function",string_to_reverse,"et sa longueur ",len(string_to_reverse))) fonctionnel
  # sans global, j'obtiendrai l'erreur : UnboundLocalError: local variable 'string_reversed' referenced before assignment
  # soit je procède ainsi avec global devant ma variable utilisé dans ce contexte (car elle a été déclarée avant ma fonction), soit je la déclare directement dans la fonction sans global, alors dans tel cas il ne faut pas la déclarer avant la fonction
  global string_reversed
  for character in string_to_reverse:
    # print(character,end="") # fonctionnel
    # string_reversed = character + string_reversed # fonctionnel
    if (character != " "): string_reversed = character + string_reversed # fonctionnel aussi, pour échapper les espaces
  print()
  return string_reversed

string_reversed = function_to_reverse_string("Voici une chaîne au hasard")
# pour corriger l'erreur levée par l'interpréteur de Python, j'ai assigné le rétour de la fonction dans ma variable

print("string_reversed avant utilisation de la méthode split() :",string_reversed)

# The \s character matches Unicode whitespace characters like [ \t\n\r\f\v]

print("string_reversed avant utilisation de la méthode split() :",string_reversed)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
"""
en sortie :
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

print()

#---------------------------------------- fonctionnels aussi ---------------------------------------- 

# avant la version 3.10 de Python, il n'y avait pas de match case possible, donc if / elif / else
# la fonction rate_note() avec if / elif / else
def rate_note(n):
  retour=""
  if n>=0 and n <10:
    retour = "c'est une mauvaise note"
  elif n==10:
    retour="c'est juste la moyenne, bof !"
  elif n>10 and n<20:
    retour='bon travail, persistez, et ça le fera :)'
  elif n == 20:
    retour="c'est excellent ! continuez-ainsi !"
  else:
    retour="c'est quoi cette note, je ne comprends pas :("
  return retour

note_test=20

retour=rate_note(note_test)
print(F"avec une note de {note_test}, voici ce que j'en dit : {retour}")
"""
en sortie :
  avec en entrée -5 : avec une note de -5, voici ce que j'en dit : c'est quoi cette note, je ne comprends pas :(
  avec en entrée 0 : avec une note de 0, voici ce que j'en dit : c'est une mauvaise note
  avec en entrée 5 : avec une note de 5, voici ce que j'en dit : c'est une mauvaise note
  avec en entrée 9 : avec une note de 9, voici ce que j'en dit : c'est une mauvaise note
  avec en entrée 10 : avec une note de 10, voici ce que j'en dit : c'est juste la moyenne, bof !
  avec en entrée 11 : avec une note de 11, voici ce que j'en dit : bon travail, persistez, et ça le fera :)
  avec en entrée 15 : avec une note de 15, voici ce que j'en dit : bon travail, persistez, et ça le fera :)
  avec en entrée 19 : avec une note de 19, voici ce que j'en dit : bon travail, persistez, et ça le fera :)
  avec en entrée 20 : avec une note de 20, voici ce que j'en dit : c'est excellent ! continuez-ainsi !
  avec en entrée 21 : avec une note de 21, voici ce que j'en dit : c'est quoi cette note, je ne comprends pas :(   
"""

print()

# depuis la version 3.10 de Python, match case possible
# la fonction rate_note_1() avec match case possible
def rate_note_1(note):
  retour=""
  match note:
    case 0,1,2,3,4,5,6,7,8,9 :
      retour = "c'est une mauvaise note"
    case 10:
      retour="c'est juste la moyenne, bof !"
    case 11, 12, 13, 14, 15, 16, 17, 18, 19:
      retour='bon travail, persistez, et ça le fera :)'
    case 20:
      retour="c'est excellent ! continuez-ainsi !"
    case _:
      retour="c'est quoi cette note, je ne comprends pas :("
  return retour

result=rate_note_1(note_test)
print(F"avec une note de {note_test}, voici ma réponse : {retour}")

#---------------------------------------------------------------------------------------------------- 

# calculatrice fonctionnelle
print()
def make_calcul(nb1,nb2,op):
  result=""
  if type(nb1)==int and type(nb2)==int:
    if op=="+" or op=="-" or op=="*" or op=="/":
      match op:
        case "+":
          result=nb1+nb2
        case "-":
          result=nb1-nb2
        case "/":
          if(nb2>0):
            result=nb1/nb2
          else:
            result="on ne peut pas diviser par 0 - opération impossible"
        case "*":
          result=nb1*nb2
        case _:
          result="je ne peux pas effectuer le calcul demandé !"
    else:
      result="je ne peux pas effectuer le calcul demandé !"
  else:
    result="je ne peux pas effectuer le calcul demandé !"
  return result

nb1=9
nb2=5
operator = "*"
retour_calcul = make_calcul(nb1,nb2,operator)
print(f"voici le résultat {nb1} {operator} {nb2} = {retour_calcul}")
print()
#----------------------------------------------------------------------------------------------------

# utilisation de la boucle while() - while loop - fonctionnelle

value_max = 7
current_value=1
while current_value<=7:
  print(f"la valeur de la current_value est de {current_value}")
  current_value += 1
print("la boucle while a pris fin")

"""
en sortie :
la valeur de la current_value est de 0
la valeur de la current_value est de 1
la valeur de la current_value est de 2
la valeur de la current_value est de 3
la valeur de la current_value est de 4
la valeur de la current_value est de 5
la valeur de la current_value est de 6
la valeur de la current_value est de 7
la boucle while a pris fin
"""
print()

# utilisation de break pour interrompre la suite d'exécution de la boucle avant ce qui était prévu - fonctionnel
for i in range(7):
  if(i==5):
    break
  print("i ",i)

"""
en sortie :
i  0
i  1
i  2
i  3
i  4
"""

# utilisation de continue pour poursuivre la suite d'exécution de la boucle sans exécuter le cas où l'instruction continue a été fourni - fonctionnel
print()
# range(1,7) - la boucle s'effectuera en commençant par 1 et en allant jusqu'à 6 (car 1 est inclus, et 7 est exclu)- lorsque i vaudra 5 la valeur de i ne sera pas affiché, on poursuit directement sur l'itération suivante de la boucle
for i in range(1,7):
  if(i==5):
    continue
  print("i ",i)

"""
en sortie :
i  1
i  2
i  3
i  4
i  6
"""

# autres fonctions fonctionnelles (sans paramètres, avec paramètre, puis avec paramètre et retour lorsque le prénom Christophe est envoyé à la fonction)
"""
Est-ce qu’une fonction peut renvoyer plusieurs valeurs simultanément ?
Il est possible de retourner plusieurs valeurs en les séparant par des virgules dans l'instruction de retour de la fonction.
Les valeurs retournées seront automatiquement regroupées dans un tuple.Quand utiliser les fonctions
"""

print()

def affiche_bonjour():
  print("Bonjour")

affiche_bonjour()

def affiche_bonjour_avec_prenom(prenom):
  '''méthode pour retourner le message Bonjour suivi du prénom passé en paramètre'''
  print(f"Bonjour {prenom}")

affiche_bonjour_avec_prenom("Christophe")

def affiche_bonjour_avec_prenom_et_retour(prenom):
  retour=""
  if prenom=="Christophe":
    retour="Salut, mon ami :)"
  else:
    retour=""
  return print("Bonjour",prenom,retour) # presque optionnel en fait, si on commente cette ligne avec le return cela fonctionnera aussi

affiche_bonjour_avec_prenom_et_retour("Christophe")

print()

# tout ce qui suit est fonctionnel aussi

# utilisation de documentation docstring
"""
Les docstrings sont des chaînes de documentation qui sont utilisées pour documenter les fonctions, les modules, les classes et les méthodes dans le code.
Elles sont généralement placées directement après la déclaration de la fonction, de la classe, du module ou de la méthode, entre des guillemets triples.
Pour faire s'afficher la dostring concernant la fonction, il suffit de faire dans ce cas ici : help(calcul_salaire_horaire) avec l'interpréteur de Python
"""

def calcul_salaire_horaire(salaire_mensuel, nb_heures_travaillees_par_semaine):
  """
  Cette fonction calcule le taux horaire en se basant sur les deux paramètres qui lui sont fournis, et retourne le résultat.

  Parameters:
  salaire_mensuel (int ou float): le premier paramètre
  nb_heures_travaillees_par_semaine (int ou float): le deuxième paramètre

  Returns:
  int ou float: le salaire horaire
  """
  salaire_horaire=0
  try:
    if ( ((type(salaire_mensuel)==int or type(salaire_mensuel)==float)) and ((type(nb_heures_travaillees_par_semaine)==int or type(nb_heures_travaillees_par_semaine)==float)) and (salaire_mensuel>0) and (nb_heures_travaillees_par_semaine>0) ):
      salaire_horaire = salaire_mensuel * 12 / 52 / nb_heures_travaillees_par_semaine
    else: print("Erreur, je ne peux effectuer ce calcul")
    # break lorsque la fonction n'a pas de valeur à retourner via un return
    return salaire_horaire
  except (RuntimeError, TypeError, NameError, ZeroDivisionError):
    # pass - si je ne souhaite pas afficher de message en particulier
    print("Au moins l'un des deux n'est pas un nombre !")

print(calcul_salaire_horaire(26933/12,35)) # 26933 / 12 = 2244.42
print()


salaire_mensuel_test=21000/12
nb_heures_semaine_test=0
if (salaire_mensuel_test>0 and nb_heures_semaine_test>0): print("line887",calcul_salaire_horaire(21000/12,0))
# en sortie : 
# Au moins l'un des deux n'est pas un nombre !
# line887 None

print()
'''
print(calcul_salaire_horaire(2244,35))
en sortie :
  avec en entrée 2244,35 (2244 le salaire mensuel et 35 le nb d'heures hebdromadaire) : 14.795604395604395
print(calcul_salaire_horaire(21000/12,35)) # 21000 / 12 = 1750
  avec en entrée 21000/12,35 (21000/12=1750 le salaire mensuel et 35 le nb d'heures hebdromadaire) : 11.538461538461538
'''
def calcul_salaire_horaire_arrondi(salaire_mensuel, nb_heures_travaillees_par_semaine):
  salaire_horaire=0
  if (salaire_mensuel and nb_heures_travaillees_par_semaine):
    salaire_horaire = round(salaire_mensuel * 12 / 52 / nb_heures_travaillees_par_semaine, 2) # utilisation de round(nb,2) pour un arrondi à deux décimales
  else: print("Erreur, je ne peux effectuer ce calcul")
  return salaire_horaire

print(calcul_salaire_horaire_arrondi(21000/12,35)) # 21000 / 12 = 1750 en sortie : salaire horaire arrondi à 11.54
print(calcul_salaire_horaire_arrondi(2244,35)) # en sortie : salaire horaire arrondi à 14.8
print()

print(affiche_bonjour_avec_prenom.__doc__) # pour voir s'afficher la docstring sur cette méthode (équivalent à JavaDoc mais pour Python)
# affiche : méthode pour retourner le message Bonjour suivi du prénom passé en paramètre

print(calcul_salaire_horaire.__doc__)

print()

# fonctionnel - source : https://docs.python.org/fr/3/tutorial/errors.html
"""
while True:
  try:
    x = int(input("Veuillez entrer un nombre s'il vous plaît : "))
    break
  except ValueError:
    print("Ce n'est pas un nombre valide")
"""




