# Atributos de classe
# __dict__ e vars para atributos de instância.

ano_atual = 2022
class Pessoa:
    ano_atual = 2022 # Observe q se mudar o valor da variável ela muda para toda a classe.

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def ano_nasc(self):
        print(self.ano_atual - self.idade)


p1 = Pessoa('jao', 33)
p1.__dict__['outra'] = 'coisa'
#p1.__dict__['name'] = 'Eita'
#Pessoa.ano_nasc(p1)
#p1.ano_nasc()
#print(p1.__dict__)
print(vars(p1)) # Vai chamar o __dict__ = Dados da variável.
print(p1.outra)
#print(p1.name)