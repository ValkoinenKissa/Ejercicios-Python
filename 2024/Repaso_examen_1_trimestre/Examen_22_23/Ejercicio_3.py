num_pin = 8947
stop = False
intentos = 3

while not stop:
    pin_usuario = int(input(f"Introduce tu numero pin, tienes {intentos} intentos"))
    if num_pin == pin_usuario:
        print("Has iniciado sesion en tu cuneta correctamente.")
        stop = True

    else:
        intentos = intentos - 1
        print(f"El pin no es correcto")
        if intentos == 0:
            print("Te has quedado sin intentos")
            stop = True
