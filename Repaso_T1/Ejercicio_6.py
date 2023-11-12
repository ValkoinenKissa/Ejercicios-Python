"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
impar
"""

number = int(input("Usuario, introduce un nuemero para verificar si es par o no lo es: "))

if number % 2 == 0:
    print("El numero que has introducido es par")

else:
    print("El numero que has introducido no es par")
