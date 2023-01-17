"""
Como criar módulos em python !!!
"""
from Dados import pessoas,lista

def dobra_lst(lista):    # Dobra cada valor dos elementos daa lista
    return [x*2 for x in lista]


print(dobra_lst(lista))


def mutiplica(lista): # multiplica todos os elementos da lista
    r = 1
    for i in lista:
        r *= i
    return r


print(mutiplica(lista))
