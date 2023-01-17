def leiaint(msg):
  while True:
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
      print('ERRO: por favor, digite um número válido.')
      continue
    except (KeyboardInterrupt):
      print('O usuário não quis digitar esse número')
      return 0
    else:
      return n

def leiafloat(msg):
  while True:
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
      print('ERRO: por favor, digite um número válido.')
      continue
    except (KeyboardInterrupt):
      print('O usuário não quis digitar esse número')
      return 0
    else:
      return n

num1 = leiaint('Digite um valor: ')
num2 = leiafloat('Digite outro valor: ')
print(f'o valor digitado foi {num1} e {num2}')