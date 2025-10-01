"""
Realizar un programa que permita crear un diccionario inglés / castellano. La clave es la palabra
en inglés y el valor es la palabra en castellano. Crear funciones para cargar el diccionario, listar el
diccionario. Crear una tercera función que solicite la carga por teclado de una palabra en inglés,
mostrar después el valor en castellano si este existe.
"""


def crear_diccionario(diccionario):
    num_elementos = int(input("Introduce el numero de traducciones que quieres crear"))
    for i in range(0, num_elementos):
        eng = str(input("Introduce la palabra en ingles"))
        esp = str(input("Introduce la plabra es español asociada a la palabra en ingles"))
        diccionario[esp] = eng


def imprimir_diccionario(diccionario):
    for valor in diccionario:
        print("Ingles: ", valor, "-->", "Español ", diccionario[valor])


def buscar_valor(diccionario):
    valor = input("Introduce la palabra en inglés que quieres buscar: ")
    if valor in diccionario:
        print("El valor buscado es:", diccionario[valor])
    else:
        print("No se ha encontrado la palabra que has introducido en el diccionario")


def main():
    diccionario = dict()
    crear_diccionario(diccionario)
    imprimir_diccionario(diccionario)
    buscar_valor(diccionario)


main()
