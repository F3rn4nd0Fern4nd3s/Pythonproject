def lin(tam=42):
    return '-' * tam

def cabeca(txt):
    print(lin())
    print(txt)
    print(lin())

cabeca('Menu principal'.center(42))