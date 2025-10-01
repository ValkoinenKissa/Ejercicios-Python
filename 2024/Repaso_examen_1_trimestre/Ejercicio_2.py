"""
Diseña una función que calcule y devuelva el factorial de un número entero. Sabemos que:
!0 es 1, 5! = 5 * 4 * 3 * 2 * 1
"""


def intro_datos():
    num = int(input("Introduce un dato para hacer su conversion a factorial: "))
    return num


def hacer_factorial(num):
    acum = 1
    for i in range(1, num+1):
        acum *= i
    return acum


def imprime_results(acum):
    print(f"El factorial del numero introducido es: {acum}")


def main():
    numero = intro_datos()
    factorial = hacer_factorial(numero)
    imprime_results(factorial)


main()
