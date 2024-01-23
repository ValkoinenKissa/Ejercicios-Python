"""
Diseña una clase Vehiculo. Sus datos son: marca, modelo, motor, color,
número de ruedas. Escribe un constructor, los métodos set, y una función
que muestre en pantalla los datos de un vehículo. Construye unas subclases
de Vehiculo, denominadas Coche y Camión. Los datos adicionales son
respectivamente: número de pasajeros y límite de carga.
"""


class Vehiculo:
    def __init__(self, marca, modelo, motor, color, num_ruedas):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__color = color
        self.__num_ruedas = num_ruedas

    # Getters y setters

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_motor(self, motor):
        self.__motor = motor

    def get_motor(self):
        return self.__motor

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_num_ruedas(self, num_ruedas):
        self.__num_ruedas = num_ruedas

    def get_num_ruedas(self):
        return self.__num_ruedas

    def __str__(self):
        return (f"Marca: {self.__marca}, Modelo: {self.__modelo}, Motor: {self.__motor}, Color: {self.__color}, Num "
                f"ruedas: {self.__num_ruedas}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, motor, color, num_ruedas, num_pasajeros):
        super().__init__(marca, modelo, motor, color, num_ruedas)
        self.__num_pasajeros = num_pasajeros

    # Getters y setters

    def set_num_pasajeros(self, num_pasajeros):
        self.__num_pasajeros = num_pasajeros

    def get_num_pasajeros(self):
        return self.__num_pasajeros

    def __str__(self):
        return super().__str__() + f" El numero de pasajeros que puede llevar el coche es: {self.__num_pasajeros}"


class Camion(Vehiculo):
    def __init__(self, marca, modelo, motor, color, num_ruedas, limite_carga):
        super().__init__(marca, modelo, motor, color, num_ruedas)
        self.__limite_carga = limite_carga

    # Getters y setters
    def set_limite_carga(self, limite_carga):
        self.__limite_carga = limite_carga

    def get_limite_carga(self):
        return self.__limite_carga

    def __str__(self):
        return super().__str__() + f" El limite de carga del cambion es de: {self.__limite_carga}"


def main():
    mi_coche = Coche("Toyota", "Corolla", "180H HEV", "Gris", "4", "5")
    mostar_coche = str(mi_coche)
    print(mostar_coche)
    mi_camion = Camion("Volvo", "DH", "600H", "Blanco", "8", "7")
    mostrar_camion = str(mi_camion)
    print(mostrar_camion)


main()
