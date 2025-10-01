"""
2) Dado el código siguiente:
cadena = "La insoportable levedad del ser"
print(quitar_blancos(cadena))
Desarrolla la función quitar_blancos(cadena)
baremo: 2 puntos
"""


def quitar_blancos(cadena):
    nueva_cadena = ""
    for letras in cadena:
        if letras != " ":
            nueva_cadena += letras
    return nueva_cadena


def main():
    cadena = str(input("Introduce una cadena para quitar los espacios en blanco: "))
    cadena_sin_blancos = quitar_blancos(cadena)
    print(cadena_sin_blancos)


main()
