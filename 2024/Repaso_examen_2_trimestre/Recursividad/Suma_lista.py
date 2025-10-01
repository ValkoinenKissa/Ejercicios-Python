def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


def main():
    lista = [1, 2, 3, 4, 5]
    resultado = suma_lista(lista)
    print(f"La suma de la lista es {resultado}")


main()