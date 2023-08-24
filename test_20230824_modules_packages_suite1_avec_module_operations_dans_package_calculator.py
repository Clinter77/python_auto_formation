# import du module operations qui se situe dans le package calculator - ici j'importe tout ce qui se trouve dans mon module operations
# import calculator.operations

# on peut aussi utiliser from pour importer une ou plusieurs fonctions du module
from calculator.operations import multiplication

if __name__ == '__main__':
    # resultat = calculator.operations.sum(10, 30)
    resultat = multiplication(10, 30)
    print("resultat:",resultat)

