"""
Diseña una función que calcule y devuelva el factorial de un número entero. Sabemos que:
!0 es 1, 5! = 5 * 4 * 3 * 2 * 1
"""


def intro_num():
    num = int(input("Introduce un numero para calcular su factorial: "))
    return num


def cacl_factorial(num):
    acum = 1
    for i in range(1, num + 1):
        acum *= i

    return acum


def muestra_resultado(acum):
    print(f"El factorial del numero que has introducido es: {acum}")


def main():
    num = intro_num()
    factorial = cacl_factorial(num)
    muestra_resultado(factorial)


main()
