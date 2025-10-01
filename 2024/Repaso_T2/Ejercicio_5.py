"""
Diseña una función que calcule y devuelva el factorial de un número entero. Sabemos que:
!0 es 1, 5! = 5 * 4 * 3 * 2 * 1
"""


def intro_num():
    num = int(input("Introduce un numero para calcular su factorial: "))
    return num


def factorial(num):
    if num <= 0:
        return 1
    else:

        return num * factorial(num - 1)


def imprime_los_results(resultado, num):
    print(f"El factorial de {num} es {resultado}")


def main():
    numero_introducido = intro_num()
    calc = factorial(numero_introducido)
    imprime_los_results(calc, numero_introducido)


main()
