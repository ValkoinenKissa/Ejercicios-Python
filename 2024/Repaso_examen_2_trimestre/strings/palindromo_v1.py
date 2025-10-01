def es_palindromo(cadena):
    copy = ""
    for letra in range(len(cadena)):
        copy = cadena[letra] + copy

    if copy == cadena:
        return True
    else:
        return False


def main():
    cadena = str(input("Introduce una cadena para comprobar si es un palindromo: "))
    resultado = es_palindromo(cadena)
    if resultado:
        print("El string que has introducido es un palindromo!!!")

    else:
        print("Es texto que has introducido no es un palindromo")


main()
