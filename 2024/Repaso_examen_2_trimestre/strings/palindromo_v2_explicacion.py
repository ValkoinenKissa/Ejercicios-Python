def es_palindromo(cadena):
    # Calcula la última posición en la cadena (resta 1 ya que los índices en Python comienzan desde 0)
    ultima_posicion = len(cadena) - 1

    # Itera hasta la mitad de la longitud de la cadena (redondeando hacia arriba)
    for i in range(ultima_posicion // 2 + 1):
        # Compara el carácter en la posición i con el carácter en la posición opuesta
        if cadena[i] != cadena[ultima_posicion - i]:
            # Si no coinciden, la cadena no es un palíndromo, retorna False
            return False

    # Si el bucle se completa sin retornar False, la cadena es un palíndromo, retorna True
    return True


def main():
    cadena = str(input("Introduce una cadena: "))
    resultado = es_palindromo(cadena)

    if resultado:
        print("Es un palindromo!!")

    else:
        print("No es una palindromo....")


main()
