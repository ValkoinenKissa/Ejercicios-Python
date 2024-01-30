"""
Realizar un programa que contenga una lista con 10 valores enteros. Informar de cuántos de ellos
son superiores a 100.
"""

import random

valores_enteros = []

for i in range(0, 11):
    valores_enteros.append(random.randint(0, 150))

print(f"Imprimir la lista: {valores_enteros}")
contador = 0
for valores in valores_enteros:
    if valores > 100:
        contador += 1

print("El numero de valores en el array superiores a 100 son: ", contador)
