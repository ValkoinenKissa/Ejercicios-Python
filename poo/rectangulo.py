
class Rectangulo:
    #constructor
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura


    #métodos set
    def set_base(self, base):
         self.__base = base


    def set_altura(self, altura):
            self.__altura = altura

    #métodos get
    def get_base(self):
        return self.__base


    def get_altura(self):
        return self.__altura


    def mostrar_datos(self):
            print("base:", self.__base)
            print("altura:", self.__altura)


    def area(self):
        return self.__base * self.__altura


    def perimetro(self):
        return 2 * (self.__base + self.__altura)


    def clonar(self, rectang):
       return Rectangulo(rectang.__base, rectang.__altura)



def main():
    #instanciamos un objeto de tipo Rectangulo
    rect1 = Rectangulo(4,2)
    rect1.mostrar_datos()
    print("área = ", rect1.area())
    print("perímetro = ", rect1.perimetro())
    #modificamos aributos
    rect1.set_base(7)
    rect1.set_altura(2)
    print("área = ", rect1.area())
    print("perímetro = ", rect1.perimetro())
    #print("base = ",rect1.base)
    print("base = ", rect1.get_base())
    #clonamos un objeto y hacemos un paso de parámetros por referencia
    rect2 = rect1.clonar(rect1)
    rect2.mostrar_datos()
    #imprimir las referenias
    print("Referencias de los objetos")
    print(rect1)
    print(rect2)




main()
