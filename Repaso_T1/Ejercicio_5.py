"""
Escribir un programa que pida al usuario dos números float y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))


if num1 == 0 and num2 == 0:
    print("ERROR, no puedes dividir un numero entre 0, por favor introduce de nuevo los valores")
    while num1 and num2 == 0:
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))
        division = num1 / num2
        print("El resultado es: ", division)
else:
    division = num1 / num2
    print("El resultado es: ", division)

