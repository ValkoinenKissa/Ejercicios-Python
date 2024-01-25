"""
Diseña una función que retorne un valor que indique si una cadena es un palíndromo. Un
palíndromo (del griego palin dromein, 'volver a ir atrás'), también llamado palindromo, palíndroma
o palindroma, es una palabra o frase que se lee igual en un sentido que en otro (por ejemplo, Ana).
Si se trata de números en lugar de letras, se llama capicúa. Otro ejemplo: “amadaladama”....
"""


def es_palindromo(cadena):
    copy = ""
    for letra in range(len(cadena)):
        copy = cadena[letra] + copy

    return copy == cadena


def main():
    cadena = str(input("Introduce un texto para comprobar si es palindromo"))
    resultado = es_palindromo(cadena)

    if resultado:
        print("El texto que has introducido es un palindromo")
    else:
        print("El texto no es palindromo")


main()
