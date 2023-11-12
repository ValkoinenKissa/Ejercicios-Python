"""
Diseña una aplicación que permita trabajar con objetos de tipo Cuenta.
Los datos de una cuenta son: número de cuenta, nombre de titular, saldo y
tipo de interés. Escribe un constructor, los métodos set, y los métodos
ingreso y reintegro que permitan ingresar y sacar una cantidad de la
cuenta. También una función que muestre en pantalla los datos de una
cuenta. Sería interesante tener una función que imprima en pantalla las
operaciones que se pueden hacer con una cuenta: consultar el saldo,
ingreso, reintegro, mostrar todos sus datos y salir de la aplicación:
"""

class Cuenta:
    def __init__(self, num_cuenta, nombre_titular, saldo, tipo_interes):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo
        self.tipo_interes = tipo_interes

    def mostrar_datos(self):
        print("Esta es tu posición global, aquí puedes ver los detalles de tu cuenta: ")
        print(f"Número de cuenta: {self.num_cuenta}")
        print(f"Titular de la cuenta: {self.nombre_titular}")
        print(f"Saldo actual: {self.saldo}")
        print(f"Tipo de interés: {self.tipo_interes}")

    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")


    def reintegro(self, cantidad):
        if cantidad > 0:
            self.saldo -= cantidad
            print(f"Reintegro de {cantidad} realizado. Nuevo saldo: {self.saldo}")

        else:
            print("La cantidad que deseas retirar debe ser mayor que 0")

    def menu_opciones(self, opcion):



def main():
    # Crear una instancia de la clase Cuenta
    mi_cuenta = Cuenta("ES2345678901234567890", "Alberto Bollo", 50, 0)

    # Mostrar datos
    mi_cuenta.mostrar_datos()

    # Ingresar dinero
    cantidad_ingreso = float(input("Introduce la cantidad que deseas ingresar: "))
    mi_cuenta.ingresar_dinero(cantidad_ingreso)

    # reintegro dinero
    cantidad_reintegro = float(input("Introduce la cantidad que deseas retirar: "))
    mi_cuenta.reintegro(cantidad_reintegro)


if __name__ == "__main__":
    main()
