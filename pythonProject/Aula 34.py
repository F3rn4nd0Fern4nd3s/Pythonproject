def lin():
    print('--'*30)
t = 'Teste de perguntas e repostas'
print(t.upper())
lin()
acertos = 0
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5', 'd': '100', 'e': '25'},
        'resposta_certa': 'b',
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 12 x 10? ',
        'respostas': {'a': '10', 'b': '40', 'c': '60', 'd': '120', 'e': '25'},
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 22 + 22? ',
        'respostas': {'a': '11', 'b': '44', 'c': '55', 'd': '100', 'e': '25'},
        'resposta_certa': 'b',
    },
    'Pergunta4': {
        'pergunta': 'Quanto é 222 + 222? ',
        'respostas': {'a': '111', 'b': '444', 'c': '555', 'd': '1000', 'e': '255'},
        'resposta_certa': 'b',
    },
}

for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'({rk}): {rv}')
    print()
    resp_usu = input('A resposta é: ')
    lin()

    if resp_usu == pv['resposta_certa']:
        print('Boa você acertou ::)'.upper())
        acertos += 1

    else:
        print('IIXIIIII Você errou.'.upper())

    lin()

print(f'o números de acertos foi {acertos}/4.')