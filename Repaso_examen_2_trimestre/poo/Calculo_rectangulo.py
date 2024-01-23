class Rectangulo:
    # constructor
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # Setters

    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    # Getters

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calcular_area(self):
        area = self.__base * self.__altura
        print("El area de el rectangulo es: " + str(area))

    def calcular_perimetro(self):
        perimetro = 2 * self.__base + 2 * self.__altura
        print("El perimetro de el rectangulo es: " + str(perimetro))


def main():
    rect1 = Rectangulo(int(input("Introduce la base del rectangulo: ")), int(input("Introduce la altura del "
                                                                                   "rectangulo: ")))
    rect1.calcular_area()
    rect1.calcular_perimetro()


main()
