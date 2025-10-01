"""
Realizar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un
entero, el segundo es una lista con dos enteros, etc. La lista debería tener la siguiente estructura
[[1], [1, 2], [1, 2, 3], …]

"""

lista = []
lista_aux = []

for i in range(1, 51):
    lista_aux.append(i)
    lista.append(lista_aux[:])

print(lista)
