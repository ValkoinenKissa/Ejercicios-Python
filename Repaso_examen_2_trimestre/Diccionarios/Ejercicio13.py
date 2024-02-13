"""
Realizar un programa que permita cargar un código de producto como clave en un diccionario.
Guardar para esta clave el nombre del producto, el precio y el total disponible en stock.
Después de
ingresar un producto, preguntar si se desea cargar otro, el límite de productos lo dispondrá el
usuario.
Mostrar el listado de productos, una tercera para consultar un producto mediante su clave y
otra para mostrar el listado de productos con stock 0. Ejemplo de ejecución:
"""


def cargar_diccionario(diccionario):
    stop = False
    while not stop:
        condicion = input("Introduce los datos de inventario, para continuar introduce una Y, de lo contrario "
                          "introduce una N")
        if condicion.upper() == "Y":
            codigo = int(input("Introduce el codigo asociado al producto: "))
            nombre_producto = input("Introduce el nombre del producto: ")
            precio = int(input("Introduce el precio de los prodcutos: "))
            stock = int(input("Introduce el numero de stock de los prodcutos: "))
            diccionario[codigo] = [nombre_producto, precio, stock]
        else:
            print("Hasta pronto!!")
            stop = True

    return diccionario


def mostar_productos(diccionario):
    for cod in diccionario:
        print(cod, diccionario[cod][0], diccionario[cod][1], diccionario[cod][2])


def buscar_producto(diccionario):
    proc_buscado = int(input("Introduce el codigo del producto del que quieres mostrar sus datos: "))
    if proc_buscado in diccionario:
        print(diccionario[proc_buscado][0], diccionario[proc_buscado][1], diccionario[proc_buscado][2])


def mostar_sin_stock(diccionario):
    print("Mostrando los productos que no disponen de exitencias: ")
    for cod in diccionario:
        if diccionario[cod][2] == 0:
            print(cod, diccionario[cod][0], diccionario[cod][1], diccionario[cod][2])


def main():
    diccionario = {}
    datos = cargar_diccionario(diccionario)
    mostar_productos(datos)
    buscar_producto(datos)
    mostar_sin_stock(datos)


main()
