class Lista:
    def __init__(self, lista):
        self.lista = []

    def cargar_lista(self):
        stop = False
        while not stop:
            dato = input("Introduce los datos que quieras cargar en la lista: ")
            if dato == "fin":
                stop = True
            elif not stop:
                self.lista.append(dato)
        return self.lista

    def imprimir_lista(self):
        for elemento in self.lista:
            print(elemento)

    def consulta_secuencial(self):
        buscado = input("Introduce los datos que quieres buscar: ")
        posicion = self.busqueda_secuencial(buscado)
        existe = posicion != -1

        if existe:
            print("Encontrado ", buscado, " en la posicion ", posicion)

        else:
            print("No se ha encontrado el elemento en la lista")

    def busqueda_secuencial(self, elemento):
        encontrado = False

        for item in self.lista:
            if item == elemento:
                encontrado = True

        return encontrado

    def ordenar(self):
        intercambio = True
        while intercambio:
            intercambio = False
            for i in range(len(self.lista) - 1):
                if self.lista[i] > self.lista[i + 1]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i + 1]
                    self.lista[i + 1] = aux
                    intercambio = True

    """
        def busqueda_binaria(self, buscado):
        izq = 0
        derecha = len(self.lista) - 1
        central = (izq + derecha) // 2
        while izq <= derecha and buscado
    """

    def menu_programa(self):
        print("--------------------------------")
        print("Menu listas")
        print("1- Cargar lista")
        print("2- Imprimir")
        print("3- Busqueda secuencial")
        print("4- Ordenar lista")
        print("5- Consulta binaria")
        print("6- Salir")
        opcion = int(input("Introduce la opcion elegida...."))

        stop = False
        while not stop:

            match opcion:
                case 1:
                    self.cargar_lista()

                case 2:
                    self.imprimir_lista()

                case 3:
                    self.consulta_secuencial()

                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    stop = True

                case other:
                    print("La opcion introducida no es correcta...")


def main():
    lista_1 = []
    lista = Lista(lista_1)
    lista.menu_programa()


main()
