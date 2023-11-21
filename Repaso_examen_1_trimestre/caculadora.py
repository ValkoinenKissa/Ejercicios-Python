"""
Programar una calculadora que presente un menu con las operaciones aritméticas
básicas. Salimos del programa cuando el usuario teclee la opción salir. Utilice un boolean
para salir.
"""


def intro_opcion():
    print("Esta es la calculadora, introduce una de las siguientes opcciones: ")
    print("1- Suma")
    print("2- Resta")
    print("3- Division")
    print("4- Multiplicación")
    print("5- Salir")

    opcion = int(input("Introduce la opcion que has elegido: "))
    return opcion


def intro_numero1():
    num1 = int(input("Introduce el primer numero: "))
    return num1


def intro_numero2():
    num2 = int(input("Introduce el primer numero: "))
    return num2


def sumar_nums(num1, num2):
    suma = num1 + num2
    return suma


def resta_nums(num1, num2):
    resta = num1 - num2
    return resta


def division_nums(num1, num2):
    if num1 ==0 or num2 == 0:
        print("El 0 no es divisible, introduce otro numero por favor: ")
        intro_numero1()
        intro_numero2()

    else:
        division = num1 // num2
        return division


def multiplicacion_nums(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion


def main():
    salir = False

    while not salir:
        opcion = intro_opcion()
        if opcion > 5 or opcion < 1:
            print("La opcion no es correcta, intentalo de nuevo: ")
            intro_opcion()

        elif opcion == 5:
            salir = True

        else:

            num1 = intro_numero1()
            num2 = intro_numero2()
            resultado = 0
            match opcion:
                case 1:
                    resultado = sumar_nums(num1, num2)

                case 2:
                    resultado = resta_nums(num1, num2)

                case 3:
                    resultado = division_nums(num1, num2)

                case 4:
                    resultado = multiplicacion_nums(num1, num2)

        print(f"El resultado de la operaccion seleccionada es {resultado}")


main()