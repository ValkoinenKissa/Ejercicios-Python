"""
Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir.
Imprime la nota media siempre y cuando haya introducido alguna nota.
"""

# Inicializamos un contador y un acumulador
acum_notas = 0
num_notas = 0
stop = False
# Establecemos booleano de control del bucle
while not stop:
    nota = int(input("Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir: "))
    # Creamos estructura condicional la cual evalue si el numero introducido es igual a 0
    # Si es asi y el numero es mayor que cero se imprime la media acumulada eb acum_notas
    if nota == 0:
        if num_notas > 0:
            media = acum_notas / num_notas
            print("La media de las calificaciones introducidas es:", media)
        else:
            print("No se han introducido notas.")
        stop = True  # Salir del bucle
    # Si la nota no es igual a cero se empieza a acumular en el contador & en el acum
    else:
        acum_notas += nota
        num_notas += 1
