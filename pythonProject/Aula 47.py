"""
Uso de try e except como condicional
"""

#try = tente alguma coisa
# except  = se falhar faça isso + type error
# else = se der certo
# fiinally = vai aacontteceer indenpendente de error ou n


try :
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r  = a / b
except (ValueError, TypeError):
    print('tivemos um problema com o tipo de dado que você digitou.')
except ZeroDivisionError:
    print('Um número não pode ser dividido por zero.')
except KeyboardInterrupt:
    print('O Usuário não informou os dados.')
else:
    print(f'o Resultado é {r:.2f}')
finally:
    print('Volte sempre obrigado :)')