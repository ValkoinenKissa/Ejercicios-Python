"""
Diseña una función que calcule y devuelva el máximo común divisor de 2 números enteros
aplicando el algoritmo: cuando los números sean iguales, el máximo común divisor es cualquiera de
ellos. En caso contrario, si el número 1 es mayor que número 2, restamos al numero 1, numero 2 y
número 2 se queda igual. Si número 2 es mayor que número 1, le restamos número 1 y número 1 se
queda igual. Este proceso se repite hasta que sean iguales.
"""


def intro_num1():
    num1 = int(input("Introduce el primer numero: "))
    return num1


def intro_num2():
    num2 = int(input("Introduce el segundo numero: "))
    return num2


def calculo_mcd(num1, num2):
    if num1 == num2:
        return 1

    else:
        if num1 > num2:
            return calculo_mcd(num2, num1 - num2)


        else:
            return calculo_mcd(num1, num2 - num1)


def mostrar_resultados(num1, num2, resultado):
    print(f"El MCD de {num1} y {num2} es {resultado}")


def main():
    numero_1 = intro_num1()
    numero_2 = intro_num2()
    mcd = calculo_mcd(numero_1, numero_2)
    mostrar_resultados(numero_1, numero_2, mcd)


main()
