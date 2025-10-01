"""
Desarrolla una clase Empleado cuyos atributos sean dni y nombre. La clase tendrá un constructor
y un método que muestre en pantalla los datos de un empleado. A continuación desarrolla una clase
EmpleadoJefe cuyos atributos, además del dni y nombre incorpore el departamento que dirige. La
clase dispondrá de un constructor y de una método que muestre los datos y que se llame igual que el
método mostrar de la clase Empleado. Por ultimo, define un método main donde se instancie un
EmpleadoJefe y se muestren sus datos.

"""


class Empleado:
    def __init__(self, dni, nombre):
        self.nombre = nombre
        self.dni = dni

    def mostrar_datos(self):
        print(f"Los datos del empleado son, el nombre {self.nombre} y el dni {self.dni}")


class EmpleadoJefe(Empleado):
    def __init__(self, dni, nombre, departamento):
        super().__init__(dni, nombre)
        self.departamento = departamento

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"El empleado jefe pertenece al departamento: {self.departamento}")


def main():
    jefe = EmpleadoJefe("11928434C", "Miguel", "Directores")
    jefe.mostrar_datos()


main()
