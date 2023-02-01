"""
Problema dos parâmetros mutáveis em funções
"""

# Mutáveis = Lista, dicionários

def lista_d_clientes(clientes_iteravel, lista=None): #  Resolvendo  problema de parâmetro multáveis em funções
    if lista is None:
       lista = []
    lista.extend(clientes_iteravel)
    return lista

cliente1 = lista_d_clientes(('Joao', 'Maria', 'Eduardo'))
clientes2 = lista_d_clientes(['Marcos', 'Jonas', 'Isco'])
clientes3 = lista_d_clientes(['Matheus', 'José', 'Isabella'])

print(cliente1)
print(clientes2)
print(clientes3)