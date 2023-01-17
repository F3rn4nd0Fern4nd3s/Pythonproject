"""
Try, Except - Tratando Exceções
"""

try:
    a = 1/0
except NameError as erro:
    print('Erro do desenvolvedor.')
except (IndexError, KeyError) as erro:
    print('Erro de índice')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally: # Sempre será executado
    a = 'a'

print(a)