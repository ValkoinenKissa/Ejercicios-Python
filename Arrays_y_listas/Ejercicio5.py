"""Una funcion que cargue una lista utilizando una bandera(flag), intoducir hasta el 99 hacer una fucin que se llame
ordena y que ordene la lista de mayor a menor hacer otra funcion que utilizando funciones de la clase list inmprima
en pantaña el numero mas grade y el mas pequeño de la lista desarolla una funcion que se llame mayor que retorne el
numero mas grande de la lista sin utilizar la funcion max de la clase list desarolla una funcion que se llame menor
que retorne el numero mas pequeño de la lista sin utilizar la funcion min de la clase list"""


def cargar_lista():
    mi_lista = []
    stop = False
    flag = str(-99)
    while not stop:
        mi_lista.append(input("Carga los numeros que desea cargar, introduce un -99 para parar: "))

        for lista in mi_lista:
            if flag in lista:
                stop = True

    return mi_lista


def imprimir_lista(mi_lista):
    print("Se esta imprimiendo la lista")
    for lista in mi_lista:
        print(lista)


def ordenar_lista(mi_lista):
    mi_lista.sort(reverse=True)
    print("Lista ordenada en orden ascendente")
    for lista in mi_lista:
        print(lista)
    return mi_lista


def imprime_dato_min_y_max(mi_lista):
    print("Imprimiendo los datos maximos de la lista", max(mi_lista))
    print("Imprimiendo los datos minimos de la lista", min(mi_lista))


def menor_valor(mi_lista):
    menor = mi_lista[0]
    for i in range(1, len(mi_lista)):
        if mi_lista[i] < menor:
            menor = mi_lista[i]
    print("El menor valor de la lista es: ", menor)


def mayor_valor(mi_lista):
    mayor = mi_lista[0]
    for i in range(1, len(mi_lista)):
        if mi_lista[i] > mayor:
            mayor = mi_lista[i]
    print("El mayor valor de la lista es: ", mayor)


def main():
    rellenar_lista = cargar_lista()
    imprimir_lista(rellenar_lista)
    lista_ordenada = ordenar_lista(rellenar_lista)
    imprimir_lista(lista_ordenada)
    imprime_dato_min_y_max(rellenar_lista)
    menor_valor(rellenar_lista)
    mayor_valor(rellenar_lista)


main()
