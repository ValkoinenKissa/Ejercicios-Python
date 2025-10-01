"""
6) Realizar un programa que permita cargar n países y la cantidad de habitantes que residen en cada
uno. Imprimir cada país con su número de habitantes correspondiente.

"""


def cargar_info(diccionario):
    stop = False
    while not stop:
        print("Introduce los paises y la cantidad de habitantes de cada pais, para parar introduce una S")
        parar = input("Quieres parar? S / N")
        if parar.upper() == "S":
            stop = True
        else:
            pais = input("Introduce un pais: ")
            idioma = input("Introduce su cantidad de habitantes: ")
            diccionario[pais] = idioma

    return diccionario


def imprimir_dic(diccionario):
    for paises, idiomas in diccionario.items():
        print(paises, " --> ", idiomas)


def main():
    diccionario = {}
    info = cargar_info(diccionario)
    imprimir_dic(info)


main()
