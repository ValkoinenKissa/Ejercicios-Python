"""
Diseña una función que retorne un valor que indique si una cadena es un palíndromo. Un
palíndromo (del griego palin dromein, 'volver a ir atrás'), también llamado palindromo, palíndroma
o palindroma, es una palabra o frase que se lee igual en un sentido que en otro (por ejemplo, Ana).
Si se trata de números en lugar de letras, se llama capicúa. Otro ejemplo: “amadaladama”
"""


def es_palindromo(cadena):
    copy = ""
    for letra in range(len(cadena)):
        copy = cadena[letra] + copy

    if cadena == copy:
        return True

    else:
        return False


def main():
    cadena = str(input("Introduce una cadena para comprobar si es un palindromo: "))
    verificacion = es_palindromo(cadena)

    if verificacion:
        print("La cadena introducida es un palindromo!!")

    else:
        print("la palabra que has introducido no es un palindromo...")


main()
