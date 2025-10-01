"""
Un número entero es perfecto si la suma de sus divisores es igual al propio
número. Por ejemplo: 6 es perfecto porque 1+2+3 = 6.
Implementa un código que introduzca un número entero e imprima en pantalla si el
número es perfecto o no utilizando una función que retorne un valor que sirva para
saber si un número entero es perfecto o no.
"""


# primero introducimos el numero

def intro_numero():
    num = int(input("Introduce un numero para calcular si es perfecto"))
    return num


# procedemos a sacar los divisores del numero intro

def divisores(num):
    divisores_acum = 0
    for i in range(1, num):
        if num % i == 0:
            divisores_acum += i

    return divisores_acum


def comprobacion(num, divisores_acum):
    if divisores_acum == num:
        print(f"El numero {num} es un numero perfecto")

    else:
        print("El numero no es perfecto")


def main():
    num = intro_numero()
    num_divisores = divisores(num)
    comprobacion(num, num_divisores)


main()
