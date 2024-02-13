"""
Desarrollar una función que solicite la carga del día, mes y año y devuelva una tupla con los
valores. Implementar una segunda función que reciba la tupla generada e imprima sus datos.
"""


def intro_datos():
    dia = input("Introduce el dia de hoy: ")
    mes = input("Introduce el mes de hoy: ")
    anno = input("Introduce el año actual: ")

    datos = (dia, mes, anno)

    tupla = tuple(datos)

    return tupla


def main():
    datos = intro_datos()
    print(datos)


main()
