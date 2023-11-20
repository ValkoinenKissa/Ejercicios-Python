veces = int(input("introduce el numero de veces que quieres que se imprima los astericos: "))
# creamos un bucle while que imprima el numero de asteriscos

for i in range(1, veces + 1):
    for x in range(1, i + 1):
        print("*", end=" ")

    print()
