# inicializamos una variable booleana

respuestaValida = False

while not respuestaValida:
    respuesta = input("desea continuar (s/n)?")

    if respuesta == 's' or respuesta == 'n':
        respuestaValida = True

    else:
        print("La respuesta no es correcta, prueba de nuevo")

print("El bucle a terminado")
