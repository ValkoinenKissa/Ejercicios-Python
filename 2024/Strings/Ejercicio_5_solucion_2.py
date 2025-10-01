def es_palindromo_second(cadena):
    ultima_posicion = len(cadena) -1
    for i in range(ultima_posicion // 2 + 1):
        if cadena[i] != cadena[ultima_posicion - i]:
            return False

    return True


def limpiar_cadena(cadena):
    for i in range(len(cadena)):
        cadena = cadena.lower()
        cadena = cadena.replace(" ", "")
        cadena = cadena.replace("á", "a")
        cadena = cadena.replace("é", "e")
        cadena = cadena.replace("í", "i")
        cadena = cadena.replace("ó", "o")
        cadena = cadena.replace("ú", "u")

        return cadena


def main():
    cadena = str(input("Introduce un texto para comprobar si es palindromo: "))
    cadena_clean = limpiar_cadena(cadena)
    es_palindromo_second(cadena_clean)

    if es_palindromo_second(cadena_clean):
        print(f"El texto que has introducido {cadena_clean} es un palindromo")

    else:
        print("El texto no es palindromo")


main()
# Texto prueba --> Allí ves a Sevilla
