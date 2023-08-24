# import de mon module operations avec toutes ses fonctions
# import operations

# on peut aussi tout importer du module ainsi avec l'étoile mais c'est déconseillé
# from operations import *

# import uniquement de la méthode division de mon module operations
# from operations import division

# on peut aussi importer plusieurs fonctions du modules, juste celles-ci
from operations import division, multiplication


# pour importer un module, ses fonctions, ou ses variables

if __name__ == '__main__':
    # resultat = operations.sum(10,20)
    resultat1 = multiplication(5,20)
    print("resultat1:",resultat1)
    resultat2 = division(20,5)
    print("resultat2:",resultat2)

# exécution : py test_20230824_modules_packages_suite1.py

# en résumé : 
# import mon_module
# resultat = mon_module.ma_fonction()
# ou bien
# from mon_module import ma_fonction
# resultat = ma_fonction()

# import mon_package.mon_module
# resultat = mon_package.mon_module.ma_fonction()
# ou bien
# from mon_package.mon_module import ma_fonction   
    
    