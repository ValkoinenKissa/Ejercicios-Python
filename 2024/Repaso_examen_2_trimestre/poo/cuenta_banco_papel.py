class CuentaBanco:
    def __init__(self, numero_cuenta, nombre_titular, saldo, tipo_interes):
        self.__numero_cuenta = numero_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo = saldo
        self.__tipo_interes = tipo_interes

    # Getters y setters

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def set_nombre_titular(self, nombre_titular):
        self.__nombre_titular = nombre_titular

    def get_nombre_titular(self):
        return self.__nombre_titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_tipo_interes(self, tipo_interes):
        self.__tipo_interes = tipo_interes

    def get_tipo_interes(self):
        return self.__tipo_interes

    def ingreso(self, cantidad):
        print("Introduce la cantidad a ingresar: ")
        if cantidad < 1:
            print("No se puede ingresar 0€")
        else:
            self.__saldo += cantidad
            print("Ingreso realizado correctamente...")

    def reintegro(self, cantidad_reintegro):
        print("Introduce la cantidad que quieres retirar de la cuenta: ")
        if cantidad_reintegro > self.__saldo:
            print("No tienes suficiente saldo en la cuenta para llevar a cabo esta operación...")

        else:
            self.__saldo -= cantidad_reintegro
            print("Se ha realizado el reintegro correctamente...")

    def __str__(self):
        return (f"La cuenta consultada es: {self.__numero_cuenta}, su titular es {self.__nombre_titular}, el saldo "
                f"actual de la cuenta es de {str(self.__saldo)} y el tipo de interes asociado a la misma"
                f" es de: {str(self.__tipo_interes)}")


def main():
    mi_cuenta = CuentaBanco("ES43324", "Alberto", 500, 0)
    opcion = 0
    stop = False
    while not stop:
        print("Estas son las operaciones disponibles para utilizar: ")
        print("1-Consultar el saldo \n 2-Ingreso \n 3-Reintegro \n 4-Mostar todos los datos \n 5-Salir de la App")
        opcion = int(input("Introduce la opción: "))
        match opcion:
            case 1:
                print(f"El saldo en tiempo real es de: {mi_cuenta.get_saldo()}")
            case 2:
                cantidad = int(input("Introduce el importe que quieres ingresar: "))
                mi_cuenta.ingreso(cantidad)
            case 3:
                retirada = int(input("Introduce el importe que quieres retirar de la cuenta: "))
                mi_cuenta.reintegro(retirada)
            case 4:
                show_data = str(mi_cuenta)
                print(show_data)

            case 5:
                stop = True
                print("Has abandonado la aplicación correctamente...")


main()
