"""
Diseña una función que calcule y devuelva el máximo común divisor de 2 números enteros
aplicando el algoritmo: cuando los números sean iguales, el máximo común divisor es cualquiera de
ellos. En caso contrario, si el número 1 es mayor que número 2, restamos al numero 1, numero 2 y
número 2 se queda igual. Si número 2 es mayor que número 1, le restamos número 1 y número 1 se
queda igual. Este proceso se repite hasta que sean iguales.
"""


def intro_num_1():
    num1 = int(input("Introduce el primer numero: "))
    return num1


def intro_num_2():
    num2 = int(input("Introduce el segundo numero: "))
    return num2


def calculo_mcd(num1, num2):
    if num1 == num2:
        resultado = 1

        return resultado

    else:
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2

            else:
                num2 = num2 - num1

        return num1


def imprime_resultados(num1):
    print(f"El mcd de los valores que has introducido es: {num1}")


def main():
    numero_1 = intro_num_1()
    numero2 = intro_num_2()
    calc = calculo_mcd(numero_1, numero2)
    imprime_resultados(calc)


main()
