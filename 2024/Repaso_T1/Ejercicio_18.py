"""
Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir.
Imprime la nota media siempre y cuando haya introducido alguna nota.

"""

print("Hola profesorfizzos, introduce la nota de tus alumnos para calcular su media"
      " si deseas salir, introduce un 0")

stop_programa = False
contador = 0
acum = 0
resultado = 0
while not stop_programa:
    notas_intro = float(input(f"Introduce la nota del alumno {contador}: "))
    if notas_intro != 0:
        contador = contador + 1
        acum += notas_intro

    else:
        stop_programa = notas_intro == 0

if contador > 0:
    resultado = acum / contador
    print(f"La nota media de los alumnos que has introducido es: {resultado}")

else:
    print("No se introdujo ninguna nota. No es posible calcular la nota media.")
