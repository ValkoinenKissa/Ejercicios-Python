"""
Realizar un programa que permita cargar un código de producto como clave en un diccionario.
Guardar para esta clave el nombre del producto, el precio y el total disponible en stock. Después de
ingresar un producto, preguntar si se desea cargar otro, el límite de productos lo dispondrá el
usuario. Mostrar el listado de productos, una tercera para consultar un producto mediante su clave y
otra para mostrar el listado de productos con stock 0. Ejemplo de ejecución:


Ingrese el código de producto: 1
Ingrese el nombre del producto: mesa
Ingrese el precio del producto: 100
Ingrese el total de stock del producto: 8
Desea cargar otro producto[s/n]?s
Ingrese el código de producto: 2
Ingrese el nombre del producto: silla
Ingrese el precio del producto: 20
Ingrese el total de stock del producto: 0
Desea cargar otro producto[s/n]?n
Listado de productos
1 mesa 100.0 8
2 silla 20.0 0
Ingrese el código de articulo: 2
silla 20.0 0
Listado de productos con stock 0
2 silla 20.0 0
"""


def crear_diccionario(diccionario):
    informacion = []

    valor = int(input("Ingrese el codigo del producto: "))
    informacion.append(input("Introduce el nombre del producto: "))
    informacion.append(int(input("Introduce el precio del producto: ")))
    informacion.append(int(input("Introduce el stock del producto: ")))
    diccionario[valor] = informacion


def leer_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, valor[0], valor[1], valor[2])


def buscar_diccionario(diccionario):
    valor = int(input("Introduce el codigo del articulo que quieres buscar: "))
    if valor in diccionario:
        print("La palabra ha sido encontrada")
        print(valor, diccionario[valor][0], diccionario[valor][1], diccionario[valor][2])
    else:
        print("La palabra no ha sido encontrada")


def consultar_sin_strock(diccionario):
    for i in diccionario:
        if diccionario[i][2] == 0:
            print("No se encientra stcok del producto: ")
            print(i, diccionario[i][0], diccionario[i][1], diccionario[i][2])


def main():
    diccionario = dict()
    stop = False
    while not stop:
        crear_diccionario(diccionario)
        usuario = str(input("Desea cargar otro producto[s/n]"))
        if usuario.lower() == "n":
            stop = True
        else:
            crear_diccionario(diccionario)

    leer_diccionario(diccionario)
    buscar_diccionario(diccionario)
    consultar_sin_strock(diccionario)


main()
