"""
Diseña una aplicación que permita trabajar con objetos de tipo Cuenta.
Los datos de una cuenta son: número de cuenta, nombre de titular, saldo y
tipo de interés.

Escribe un constructor, los métodos set, y los métodos
ingreso y reintegro que permitan ingresar y sacar una cantidad de la
cuenta. También una función que muestre en pantalla los datos de una
cuenta. Sería interesante tener una función que imprima en pantalla las
operaciones que se pueden hacer con una cuenta: consultar el saldo,
ingreso, reintegro, mostrar todos sus datos y salir de la aplicación:

"""


class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, saldo, tipo_interes):
        self.__numero_cuenta = numero_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo = saldo
        self.__tipo_interes = tipo_interes

    # Getters y setters num cuenta

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    # Getters y setters titular

    def set_nombre_titular(self, nombre_titular):
        self.__nombre_titular = nombre_titular

    def get_nombre_titular(self):
        return self.__nombre_titular

    # Getters y setters saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    # Getters y setters tipo de interés

    def set_tipo_interes(self, tipo_interes):
        self.__tipo_interes = tipo_interes

    def get_tipo_interes(self):
        return self.__tipo_interes

    def ingresar_saldo(self, ingreso):
        if ingreso < 0:
            print("No puedes ingresar una cantidad que sea menor que 0")
        else:
            self.__saldo += ingreso

        return print(f"El saldo actual de la cuenta es {self.__saldo}")

    def reintegro_dinero(self, reintegro):
        if reintegro > self.__saldo:
            print("No tienes suficiente saldo en la cuenta para llevar a cabo esta operación")
        elif reintegro < 0:
            print("No puedes retirar 0€ de la cuenta...")
        else:
            self.__saldo -= reintegro

        return print(f"El saldo actual de la cuenta es {self.__saldo}")

    def __str__(self):
        return (f"La cuenta consultada pertenece a: {self.__nombre_titular}, su saldo es de: {str(self.__saldo)}€, el "
                f"numero "
                f"de cuenta asociado es: {self.__numero_cuenta} y el tipo de interes asociado al cliente e"
                f"s de: {str(self.__tipo_interes)}")


def main():
    mi_cuenta = Cuenta("ES44398436736556", "Alberto bollo", 9000, 0)

    stop = False
    while not stop:
        print("Selecciona la operacion que deseas realizar:\n 1-Mostrar saldo  \n 2-Consultar datos cuenta \n "
              "3-Realizar ingreso \n 4-Realizar reintegro \n 5-Cerrar sesión")
        opcion = int(input())
        match opcion:
            case 1:
                print(f"Tu posicion global es de: {mi_cuenta.get_saldo()}€")

            case 2:
                stringdatos = str(mi_cuenta)
                print(stringdatos)

            case 3:
                ingreso = int(input("Introduce la cantidad a ingrear: "))
                mi_cuenta.ingresar_saldo(ingreso)
            case 4:
                reintegro = int(input("Elige que cantidad quieres retirar de la cuenta: "))
                mi_cuenta.reintegro_dinero(reintegro)

            case 5:
                stop = True
                print("Has cerrado la sesión correctamente...")


main()
