"""
Diseña una superclase Figura plana para tratar los datos comunes de un
Rectangulo y Triangulo. Escribe un método area que implemente
polimorfismo
"""


class FiguraPlana:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return f"Los datos de la figura plana son , la base: {self.base} y la altura: {self.altura}"

    def calcular_area(self):
        pass


class Rectangulo(FiguraPlana):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def __str__(self):
        return f"Los datos introducidos para el rectangulo son, la base: {self.base} y la altura: {self.altura}"

    def calcular_area(self):
        area_rectangulo = self.base * self.altura
        print(f"El area del rectangulo es: {area_rectangulo}")


class Triangulo(FiguraPlana):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def __str__(self):
        return f"Los datos introducidos para el triangulo son, la base: {self.base} y la altura: {self.altura}"

    def calcular_area(self):
        area_triangulo = self.base * self.altura / 2
        print(f"El area del triangulo es: {area_triangulo}")


def main():
    base = int(input("Introduce una base"))
    altura = int(input("Introduce una altura"))
    mi_rectangulo = Rectangulo(base, altura)
    datos_rectangulo = str(mi_rectangulo)
    print(datos_rectangulo)
    mi_rectangulo.calcular_area()

    print("Ahora con los mismos datos introducidos anteriormente se calculara el area del triangulo:")

    mi_triangulo = Triangulo(base, altura)
    datos_triangulo = str(mi_triangulo)
    print(datos_triangulo)
    mi_triangulo.calcular_area()


main()
