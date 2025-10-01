"""
Realizar un programa que solicite la carga de un string por teclado. Imprimir el string separando
todos los caracteres con un espacio
"""

cadena_texto = str(input("Introduce una cadena: "))

for i in cadena_texto:
    print(i, end=" ")
