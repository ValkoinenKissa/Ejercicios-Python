"""
Diseña una clase Vehiculo. Sus datos son: marca, modelo, motor, color,
número de ruedas. Escribe un constructor, los métodos set, y una función
que muestre en pantalla los datos de un vehículo. Construye unas subclases
de Vehiculo, denominadas Coche y Camión. Los datos adicionales son
respectivamente: número de pasajeros y límite de carga.

"""


class Vehiculo:

    def __init__(self, marca, modelo, motor, color, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.color = color
        self.numero_ruedas = numero_ruedas

    def __str__(self):
        return ('Marca vehiculo: ' + self.marca + ' Modelo: ' + self.modelo + ' Motor: ' + self.motor + ' Color: '
                + self.color + ' Num ruedas: ' + self.numero_ruedas)


class Coche(Vehiculo):
    def __init__(self, marca, modelo, motor, color, numero_ruedas, numero_pasajeros):
        super().__init__(marca, modelo, motor, color, numero_ruedas)
        self.numero_pasajeros = numero_pasajeros

    def __str__(self):
        return ('Marca vehiculo: ' + self.marca + ' Modelo: ' + self.modelo + ' Motor: ' + self.motor + ' Color: '
                + self.color + ' Num ruedas: ' + self.numero_ruedas + ' Limite de carga: ' + self.numero_pasajeros)

class Camion(Vehiculo):
    def __init__(self, marca, modelo, motor, color, numero_ruedas, limite_de_carga):
        super().__init__(marca, modelo, motor, color, numero_ruedas)
        self.limite_de_carga = limite_de_carga

    def __str__(self):
        return ('Marca vehiculo: ' + self.marca + ' Modelo: ' + self.modelo + ' Motor: ' + self.motor + ' Color: '
                + self.color + ' Num ruedas: ' +self.numero_ruedas+ ' Limite de carga: ' + self.limite_de_carga)


def main():
    vehicle = Vehiculo("Volvo", "V60", "190cv", "gris", "4")
    print(vehicle)
    print()
    car = Coche("Volvo", "V60", "190cv", "gris", "4", "5 plazas")
    print(car)
    print()
    truck = Camion("Scannia", "XE70", "690cv", "gris", "4", "20 Toneladas")
    print(truck)


main()
