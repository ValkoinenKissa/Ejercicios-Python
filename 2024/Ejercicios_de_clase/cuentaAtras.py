"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas.
"""

num = int(input("Introduce un numero para iniciar su cuneta atras"))

while num >= 0:
    print(num)
    num -= 1
print("Ignicion!!")
