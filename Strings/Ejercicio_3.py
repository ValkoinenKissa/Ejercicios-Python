"""
Realizar un programa que solicite la carga de un string por teclado. Informar después del número de
espacios en blanco de que consta el string, si no tiene, el programa debe informar de ello.
PS: Tener en cuenta que un espacio sería “ “ y una cadena vacía “”.
"""

cadena = input("Introduce una cadena: ")

espacios = 0
for letra in cadena:
    if letra == " ":
        espacios += 1

if espacios == 0:
    print("No hay espacios")

else:
    print(f"El numero de espacios es de: {espacios}")

    print("Otra forma de hacerlo con un for mas complicado\n\n")

string = input("Introduce una cadena: ")
contador = 0
for i in range(len(string)):
    if string == "":
        print("La cadena esta vacia")

    else:
        print(string[i] == " ")
        contador = contador + 1
        print(f"El la possicion {i}, hay un espacio")

print("Espacios totales: ", contador)
