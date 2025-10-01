"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
los números impares desde 1 hasta ese número separados por comas.

"""

num = int(input("Introduce un numero : "))

for i in range(1, num):
    if i % 2 != 0:
        print(i, end=", ")
