"""
Verifie si un nombre est premier et affiche tous les nombres premiers
modules : 
    -isprime(p)
    -main()
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un entier p est premier
    args : 
        -p : un entier dont on cherche s'il est premier
    returns : 
        -premier : un booléen, vraie si le nbr est premier sinon faux
    """
    if p <= 1:
        return False
    premier = True
    for diviseur in range(2, int(sqrt(p)+1)):
        if p % diviseur == 0:
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    Fait des appels de test en utilisant le module isprime
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
