"""
while (Enquanto) / else - Aula 8
contadores
acumuladores
"""
# while (condição):
#   print
contador = 0 # Serve para garantir q o while terá um fim.
acumulador = 1 # você vai sommer em cada laço

while contador <= 12:
    print(contador, acumulador,end=',')
    acumulador = acumulador + contador
    contador += 3

    if contador > 5 :
        break

else:
    print('CHEGUEI NO ELSE.')