"""
Superclase
"""


class FiguraPlana:

    def __init__(self, base, altura):
        self.base = base

        self.altura = altura

    def mostrar_datos(self):
        print(f"Base {self.altura}")
        print(f"Altura {self.altura}")

    def area(self):
        pass


class Rectangulo(FiguraPlana):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def mostrar_datos(self):
        super().mostrar_datos()

    def area(self):
        return self.base * self.altura


class Triangulo(FiguraPlana):
    def __init__(self, base, altura):
        FiguraPlana.__init__(self, base, altura)

    def mostrar_datos(self):
        FiguraPlana.mostrar_datos(self)

    def area(self):
        return self.base * self.altura / 2


def main():
    fp = FiguraPlana(4, 6)
    fp.mostrar_datos()
    rect1 = Rectangulo(4, 5)
    rect1.mostrar_datos()
    print(f"Area del rectanfulo {rect1.area()}")
    tri1 = Triangulo(12, 5)
    tri1.mostrar_datos()
    print(f"Area del triangulo{tri1.area()}")


main()
