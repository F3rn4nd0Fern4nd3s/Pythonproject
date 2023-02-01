
from time import sleep

arq = 'cursoemvideo.txt'
if not arqexiste(arq):
    criararq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas','Cadastra novas Pessoas','Sair do sistema'])
    if resp == 1:
        lerarq(arq)
    elif resp == 2:
        cabeca('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cad(arq, nome, idade)
    elif resp == 3:
        cabeca('Saindo do sistema')
        break
    else:
        print('\033[31mERROR! Digite uma opção valida!\033[m')
    sleep(2)