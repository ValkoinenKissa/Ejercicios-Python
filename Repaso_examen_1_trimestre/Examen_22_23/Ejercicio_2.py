num_desconocido = 422
num_usuario = 0

stop = False

while not stop:
    num_usuario = int(input("Introduce un número para intentar adivinar el número desconocido, "
                            "si te rindes introduce un -1: "))

    if num_usuario == num_desconocido:
        print("¡Felicidades! Has adivinado el número desconocido")
        stop = True

    elif num_usuario == -1:
        stop = True

    elif num_usuario > num_desconocido:
        print("Estás lejos del resultado del número desconocido")

    else:
        print("Introduce un número más grande")

# Estas líneas se ejecutarán después de salir del bucle
print("Vuelve a jugar para intentar adivinar el número secreto")
