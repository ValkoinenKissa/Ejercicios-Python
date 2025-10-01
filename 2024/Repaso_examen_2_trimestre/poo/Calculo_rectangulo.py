"""
Diseña una aplicación que permita trabajar con objetos de tipo
Rectangulo. Utiliza un constructor, métodos set y get y añade las
operaciones de calcular el area y perímetro.
"""


class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # Getters y setters

    def set_base(self, base):
        self.__base = base

    def get_base(self):
        return self.__base

    def set_altura(self, altura):
        self.__altura = altura

    def get_altura(self):
        return self.__altura

    # Calc Area

    def calcular_area(self):
        area = self.__base * self.__altura
        return area

    def calcular_perimetro(self):
        perimetro = (self.__base * 2) + (self.__altura * 2)
        return perimetro


def main():
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))

    mi_rectangulo = Rectangulo(base, altura)

    print("El area del rectangulo es:")

    area = mi_rectangulo.calcular_area()

    print(area)

    print("El perimetro del rectangulo es: ")
    perimetro = mi_rectangulo.calcular_perimetro()
    print(perimetro)


main()
