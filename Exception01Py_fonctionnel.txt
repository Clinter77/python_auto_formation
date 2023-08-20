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
