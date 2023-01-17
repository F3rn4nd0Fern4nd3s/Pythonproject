"""
Funções decoradoras e decoradores
"""

def master():
    def slave(*args):
        print('Agora estou decorando')
    return slave

var = master
var()
print(type(var))
