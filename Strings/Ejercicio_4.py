"""
Realizar un programa que solicite la carga de un string por teclado. Imprimir el string separando
todos los caracteres con un espacio.
"""

# Forma 1

cadena = input("Introduce una cadena: ")

for letra in cadena:
    print(letra, end=" ")

# Forma 2

string = input("Ingrese una cadena de caracteres: ")

texto = ""

for x in range(len(string)):
    texto = texto + string[x] + " "
    print(string)
    print(texto)
