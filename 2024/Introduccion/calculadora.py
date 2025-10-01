# Declarar variable que controle el bucle
salir = False

while not salir:
    # Dar la bienvenida al usuario

    entrada = input(' Si guieres abandonar el programa introduce "salir" de lo contrario introduce "continuar": \n ')

    if entrada == "salir":
        print("Dale a ejecutar si quieres usar la calculadora otra vez")
        break

    else:
        num1 = float(input("Introduce el primer numero que quieres operar"))
        num2 = float(input("Introduce el segundo numero que quieres operar"))

        option = input("Ahora introduce la opcion que deseas ejecutar"
                       " \n 1- suma 2-resta 3-multiplicación 4- división 5-salir \n")
        if option != "suma, resta, multiplicacion, division, salir":
            print("Las opciones que has introducido son incorrectas, prueba de nuevo")

        else:
            match option:
                case "suma":
                    resultado = num1 + num2

                case "resta":
                    resultado = num1 - num2

                case "multiplicacion":
                    resultado = num1 * num2

                case "division":
                    if num1 == 0 or num2 == 0:
                        print("No puedes dividir un numero entre 0, intentalo de nuevo")
                    else:
                        resultado = num1 / num2

                case "salir":
                    break

            print("El resultado es: ", resultado, "Gracias por utilizar la calculadora")
