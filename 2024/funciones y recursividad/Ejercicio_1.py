"""
Diseña una función que reciba un número entero y retorne un valor que indique si el número es
par.
"""


def numero_par(num):
    if num % 2 == 0:
        print(num, "Es par")

    else:
        print(num, "no es par")

    return num


numero = numero_par(int(input("Introduce un numero para comprobar si es par o no: ")))
