# Pedimos al usuario que introduzca por pantalla la base y altura del rectangulo

altura = int(input("introduce la altura: "))
base = int(input("Introduce la base: "))
# creamos un bucle while que imprima el numero de asteriscos

for i in range(altura):
    # este bucle for imprimie la fila de asteriscos
    for x in range(base):
        print("*", end=" ")

    print()