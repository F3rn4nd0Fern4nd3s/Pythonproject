"""
função filter
"""
from Dados import produtos,lista,pessoas
def lin():
    print("=="*40)

nova_lista = filter(lambda x: x > 5,lista)
print(list(nova_lista))
lin()
nv_lst = [x for x in lista  if x > 5]
print(nv_lst)
lin()
