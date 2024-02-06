class Lista:
    def __init__(self, lista):
        self.lista = []

    def cargar_lista(self):
        stop = False
        while not stop:
            dato = input("Introduce los datos que quieras cargar en la lista: ")
            salir = (dato == "fin")
            if not salir:
                self.lista.append(dato)
        return self.lista

    def imprimir_lista(self):
        for elemento in self.lista:
            print(elemento)

    def menu_programa(self):
        opcion = 0
        stop = False
        while not stop:
            print("--------------------------------")
            print("Menu listas")
            print("1- Cargar lista")
            print("2- Imprimir")
            print("3- Busqueda secuencial")
            print("4- Ordenar lista")
            print("5- Consulta binaria")
            print("6- Salir")
            opcion = int(input("Introduce la opcion elegida...."))

        match opcion:
            case 1:
                self.cargar_lista()

            case 2:
                self.imprimir_lista()

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                stop = True

            case other:
                print("La opcion introducida no es correcta...")


def main():
    lista1 = []
    lista = Lista(lista1)
    lista.cargar_lista()
    lista.imprimir_lista()


main()
