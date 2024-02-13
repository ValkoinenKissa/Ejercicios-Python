"""
Realizar un programa que permita cargar una lista de n elementos enteros. Ordenarla de mayor a
menor e imprimir los resultados obtenidos.

"""


def cargar_lista(numeros):
    stop = False
    while not stop:
        numeros_lista = int(input("Introduce numeros enteros, Introduce un 0 cuando quieras dejar de introducir "
                                  "numeros.."))
        if numeros_lista == 0:
            break
        numeros.append(numeros_lista)

    return numeros


def ordenar_lista(numeros):
    for i in range(len(numeros)):
        min_indice = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[min_indice]:
                min_indice = j
        numeros[i], numeros[min_indice] = numeros[min_indice], numeros[i]
    return numeros


def ordenar_lista_facil(numeros):
    lista_ya_ordenada = sorted(numeros)

    return lista_ya_ordenada


def main():
    numeros = []
    lista_cargada = cargar_lista(numeros)
    lista_ordenada = ordenar_lista_facil(lista_cargada)
    print(lista_ordenada)


main()
