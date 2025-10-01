"""
Desarrolla una función que pida por pantalla un código asociado al mes. Los
códigos de mes correctos van de 1 a 12. Si el código no es correcto tiene que
visualizar un mensaje de error y volver a pedirlo. Debe de retornar un código de mes
válido. Utiliza una variable booleana para controlar el bucle.
"""


def intro_num_mes():
    stop = False
    while not stop:
        num = int(input("Introduce un numero asociado al mes: "))
        if num >= 1 and num <= 12:
            print("El numero ha quedado registrado")
            stop = True
            return num

        else:
            print("El codigo del mes no es valido, prueba de nuevo")




def main():
    num = intro_num_mes()
    print(f"El codigo del mes es {num}")

main()
