"""
Realizar un programa que permita crear un diccionario inglés / castellano. La clave es la palabra
en inglés y el valor es la palabra en castellano. Crear funciones para cargar el diccionario, listar el
diccionario. Crear una tercera función que solicite la carga por teclado de una palabra en inglés,
mostrar después el valor en castellano si este existe.
"""


def cargar_diccionario(diccionario):
    num_valores = int(input("Introduce el numero de valores que vas a introducir en el diccionario: "))
    for i in range(num_valores):
        esp = input("Introduce la palabra en español: ")
        ing = input("Introduce la palabra en inglés: ")
        diccionario[ing] = esp

    return diccionario


def listar_diccionario(diccionario):
    for eng, esp in diccionario.items():
        print(eng, " --> ", esp)


def buscar_palabra(diccionario):
    palabra_busqueda = input("Introduce la plabra que quieres traducir: ")

    encontrado = False
    traduccion = None

    for palabra in diccionario.keys():
        if palabra_busqueda == palabra:
            encontrado = True
            traduccion = diccionario[palabra]
            break

    if encontrado:
        print(f"La plabra {palabra_busqueda} ha sido encontrada, su traduccion es: {traduccion}")

    else:
        print("No se ha encontrado la traduccion de la plabra buscada...")


def main():
    diccionario = {}
    diccionario_cargado = cargar_diccionario(diccionario)
    listar_diccionario(diccionario_cargado)
    buscar = input("Quieres buscar alguna plabra en inglés en el diccionario? introduce S para si y N para no")
    if buscar.upper() == "S":
        buscar_palabra(diccionario_cargado)

    else:
        print("Adios!!")


main()
