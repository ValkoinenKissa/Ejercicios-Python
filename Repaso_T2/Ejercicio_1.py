"""
Diseña una función que reciba un número entero y retorne un valor que indique si el número es
par.
"""


def intro_numero():
    numero = int(input("Introduce un numero para comprobar si es par"))
    return numero


def comprueba_num_entero(numero):
    if numero % 2 == 0:
        print(f"Felicidades!! {numero} es un numero par")

    else:
        print(f"{numero}, no es un numero par")


def main():
    num = intro_numero()
    comprueba_num_entero(num)


main()
