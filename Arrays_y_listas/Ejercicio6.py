"""
Realizar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un
entero, el segundo es una lista con dos enteros, etc. La lista debería tener la siguiente estructura
[[1], [1, 2], [1, 2, 3], …]
"""
"""
enteros = []

count = 1

for i in range(5):
    count += 1
    num = []

    for j in range(1, count):
        num.append(i)
    enteros.append(num)

    print(enteros)
"""

# Solucion 2

lista = []
lista_auxiliar = []

for i in range(1, 5):
    lista_auxiliar.append(i)
    lista.append(lista_auxiliar[:])

print(lista)