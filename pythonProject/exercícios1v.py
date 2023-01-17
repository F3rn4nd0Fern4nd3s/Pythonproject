def lin():
    print('-'*42)

def cabe(txt):
    print(lin())
    print(txt)
    print(lin())

def menu(lista):
    cabe('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {item}')
        c += 1
        print(lin())