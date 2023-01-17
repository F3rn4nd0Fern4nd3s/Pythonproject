def soma(x: float, y: float) -> float:
    return x + y

print(__name__)
print(soma(10, 20))
print(soma(30, 20))

# se o arquivo estiver sendo executado diretamente __name__ == main.
# se o arquivo foi importado (Import) __name__ == 'nome do modulo.'