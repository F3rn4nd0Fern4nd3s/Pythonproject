"""
Reduce = soma total dos produtos
"""
from Dados import pessoas,produtos,lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # soma de todos os produtos
print(soma_lista / len(produtos)) # media

soma_idade = reduce(lambda ac, p: ac + p['Idade'], pessoas, 0) # soma de todas as idades
print(soma_idade/ len(pessoas)) # média de idades