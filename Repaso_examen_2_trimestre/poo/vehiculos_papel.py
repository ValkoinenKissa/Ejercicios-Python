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

    # Metodo para mostar datos lo heredan las otras subclases

    def mostar_datos(self):
        print(f"Los datos del vehiculo son, marca: {self.__marca}, modelo: {self.__modelo} tienen un "
              f" motor de: {self.__motor} el color es: {self.__color}, el numero de ruedas es de: {self.__num_ruedas}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, motor, color, num_ruedas, num_pasajeros):
        super().__init__(marca, modelo, motor, color, num_ruedas)
        self.__num_pasajeros = num_pasajeros

    # Getters & setters

    def set_num_pasajeros(self, num_pasajeros):
        self.__num_pasajeros = num_pasajeros

    def get_num_pasajeros(self):
        return self.__num_pasajeros

    def mostrar_datos(self):
        super().mostar_datos()
        print(f"El coche tiene espacio para {self.__num_pasajeros}, pasajeros")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, motor, color, num_ruedas, limite_carga):
        super().__init__(marca, modelo, motor, color, num_ruedas)
        self.__limite_carga = limite_carga

    def set_limite_carga(self, limite_carga):
        self.__limite_carga = limite_carga

    def get_limite_carga(self):
        return self.__limite_carga

    def mostrar_datos(self):
        super().mostar_datos()
        print(f"El camion tiene un limite de carga de: {self.__limite_carga} 7T")


def main():
    mi_coche = Coche("Toyota", "corolla", "200CV", "BLANCO", 4, 7)
    mi_coche.mostrar_datos()
    mi_camion = Camion("Volvo", "DH", "700CV", "NEGRO", 7, 9)
    mi_camion.mostrar_datos()


main()
