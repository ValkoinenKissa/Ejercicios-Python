def intro_entero():
    num = int(input("Introduce un numero: "))
    return num


def es_par(num):
    # Retornamos el resultado de una expresion booleana que permite saber si el numero es par o no
    return num % 2 == 0


def main():
    num = intro_entero()
    if es_par(num):
        print(num, "Si, si es par")

    else:
        print(num, "no, no es par")


main()
