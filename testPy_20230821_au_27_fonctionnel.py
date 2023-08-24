import random

# le tuple x
x = ("apple", "banana","cherry")
y = "#".join(x)
print("y:",y)

# s="Orange"
s = "Cette chaîne sera inversée, et selon que le nombre aléatoire généré soit pair ou impair, la lettre sera mise en majuscule, ou en minuscule !"
#s = "Cette chaîne sera inversée, on peut y placer le texte qu'on veut"

for i in range(len(s)):
    # print(s[i])
    print(s[i], end="") # pour que les caractères soient tous affichés sur la même ligne
    
i=len(s)-1
print()
print("i au départ",i)

s2=''

while i>=0:
    r = random.randrange(0,10)
    # cas impair - cette division retourne un reste avec le modulo (%)
    if (r%2 != 0):
        s2 += s[i].upper()
    # cas pair - il n'y a pas de reste après cette division
    else:
        s2 += s[i].lower()
    # print(i,"\t",s[i])
    i-=1
print("len(s2):",len(s2)," - s2:",s2)

""" 
en sortie, avec l'exemple Orange en entrée : 
y: apple/banana/cherry
O
r
a
n
g
e
i au départ 5
5        e
4        g
3        n
2        a
1        r
0        O
s2: eGnAro
"""
   
print("\n**********************\n")

# je retire les espaces vides contenus dans la chaîne - avec la boucle for i in range :
s3=""
i=0
for i in range(len(s2)):
    # print('i',i,"s2[i]",s2[i])
    if s2[i]==" ":
        continue
    else:
        s3 += s2[i]

print("len(s3):",len(s3)," - s3:",s3)
   
print("\n**********************\n")

   
# je retire les espaces vides contenus dans la chaîne, pareil, mais avec la boucle for c in my_current_string :
s3=""
for c in s2:
    if(c==" "):
        continue
    else:
        s3 += c
        
print('s3 : ',s3)
            
   
print("\n**********************\n")

str = "Christopher as often right"

if "never" in str:
    print(str,"! Don't say that")
elif 'always' in str:
    print(str,", non, on ne va pas aller jusque là :)")
else:
    print(str,", yes I agree with you :)")

"""
en sortie :
Christopher as always right , yes I agree with you :) 
ou
    Christopher as never right ! Don't say that
"""
   
print("\n**********************\n")

# Les Exceptions avec Python - Exception01

def divideAndShowResult(a,b):
    try:
        print("result:",a/b)
    # except est l'équivalent de catch
    except ZeroDivisionError as e:
        print("Il n'est pas possible de diviser par 0 !")
        print("e :",e)
    # si l'exception catchée n'est pas levée cette partie de code sera exécutée
    else:
        print("la division a bien eu lieu sans souci")
    # ce bloc de code sera toujours exécuté (Exception levée et catchée ou non)
    finally:
        print("la fin du programme")

# commentaire mono-ligne - appel de la fonction
divideAndShowResult(257,3)

"""
    - commentaires multi-lignes -
    exécution du programme avec cmd : py Exception01.py
    en entrée :
        divideAndShowResult(7,0)
    en sortie :
        Il n'est pas possible de diviser par 0 !
        e : division by zero
        la fin du programme
    en entrée :
        divideAndShowResult(257,3)
        result: 85.66666666666667
        la division a bien eu lieu sans souci
        la fin du programme
"""
   
print("\n**********************\n")

# analyser les mots d'un commentaire en échappant de celui-ci les mots considérés comme 'interdits', compris dans une liste, en les remplaçant par des ?
def analyse_and_escape_forbidden_comments(current_comment):
    list_of_forbidden_words_M = ["ANALPHABETE","BETE","DERISOIRE","ENERVANT","STUPIDE"]
    list_of_forbidden_words_m = ["analphabète","bête","dérisoire","énervant","stupide"]
    comment0_words = current_comment.split()
    comment0_after = ""

    for word in comment0_words:
        #print(word)
        if ((word.upper() in list_of_forbidden_words_M) or (word.lower() in list_of_forbidden_words_m)):
            comment0_after += "? "
        else:
            comment0_after += word+" "
    print("comment0_after:",comment0_after)

# calls of this function 
     
comment0 = "Cette stupide décision a radicalement changé les choses"
comment1 = "Ce travail lui a beaucoup apporté"
comment2 = "Cet apport est plutôt Dérisoire"
comment3 = "Cet apport est plutôt DERISOIRE"

analyse_and_escape_forbidden_comments(comment0)
# en sortie : comment0_after: Cette ? décision a radicalement changé les choses

analyse_and_escape_forbidden_comments(comment1)
# en sortie : comment0_after: Ce travail lui a beaucoup apporté

analyse_and_escape_forbidden_comments(comment2)
# en sortie : Cet apport est plutôt ?

analyse_and_escape_forbidden_comments(comment3)
# en sortie : Cet apport est plutôt ?
