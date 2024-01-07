"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
impar.
"""

print("Comprueba si un numero que has introducido es par o impar \n")

numero = int(input("Introduce tu numero: "))
resto = numero % 2

if resto == 0:
    print("El numero que has introducido es par")

else:
    print("El numero que has introducido es impar")
