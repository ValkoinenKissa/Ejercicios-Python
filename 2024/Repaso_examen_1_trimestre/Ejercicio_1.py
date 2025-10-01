def intro_datos():
    num = int(input("Introduce un numero para comborbar si el numero es par o no es par"))
    return num


def calc_par(num):
    if num % 2 == 0:
        print("El numero que has introducido es par")

    else:
        print("El numero que has introducido no es par")


def main():
    numero = intro_datos()

    calc_par(numero)


main()
