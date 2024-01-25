"""
Realizar un programa que solicite la carga de un string por teclado. Informar después del número de
espacios en blanco de que consta el string, si no tiene, el programa debe informar de ello.
PS: Tener en cuenta que un espacio sería “ “ y una cadena vacía “”.

"""

cadena_texto = str(input("Introduce una cadena: "))

contador = 0

for i in cadena_texto:
    if i == " ":
        contador += 1

    else:
        pass

print(f"La cadena introducida tenia {contador} espacios en blanco")
