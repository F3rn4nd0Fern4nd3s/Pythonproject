def lin():
    print('--'*42)

def leiaint(x):
    while True:
          n = input(x)
          if n.isnumeric():
              n = int(n)
              return n
          else:
              lin()
              print('ERROR. Por favor digite um número inteiro!')
              lin()

def leiafloat(y):
   lin()
   while True:
       try:
          n = float(input(y))
       except (ValueError,SyntaxError):
           lin()
           print('ERROR. Por favor digite um número real!')
           lin()
       else:
           return n

n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
lin()
print(f'o número inteiro é {n1} e o número real é {n2}.')
