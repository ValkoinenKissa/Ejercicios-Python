"""
4) Define un método main donde se solicite un dni y mientras no sea válido vuelva a solicitarlo.
Por último imprime en pantalla el mensaje “dni correcto”.
Un dni correcto es una cadena de 9 caracteres, donde los 8 primeros caracteres son dígitos y el
noveno es una letra que coincide con la que retornaría la función siguiente:
def letraDNI(digitos_dni):
letras="TRWAGMYFPDXBNJZSQVHLCKEO"
return letras[digitos_dni % 23]
Recuerda que la clase str tiene una función isdigit() que retorna un booleano si todos los caracteres
son dígitos, isascii() retorna un True si una carácter es una letra. Python ofrece también una
notación para identificar segmentos de una cadena.
 a[0:2]
’Ve’
 a[0:8]
’Veronica’

"""


def letra_dni(digitos_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKEO"
    return letras[digitos_dni % 23]


def main():
    stop = False
    while not stop:
        dni = input("Introduce tu dni, el programa verificara si es correcto: ")
        if len(dni) == 9:
            if dni[:8].isdigit() and not dni[8].isdigit():

                if dni[8].upper() == letra_dni(int(dni[:8])):
                    print("El dni introducido es correcto")
                    stop = True
                else:
                    print("Letra del dni no es correcta...")

            else:
                print("Comprueba la letra de tu dni por favor...")

        else:
            print("Comprueba la longitud de tu dni y prueba de nuevo")


main()
