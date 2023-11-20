"""
Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir.
Imprime la nota media siempre y cuando haya introducido alguna nota.
"""
acum_notas = 0
num_notas = 0

while True:
    nota = int(input("Introduce por teclado las notas de un conjunto de alumnos hasta que teclees un 0 para salir: "))
    if nota == 0:
        if num_notas > 0:
            media = acum_notas / num_notas
            print("La media de las calificaciones introducidas es:", media)
        else:
            print("No se han introducido notas.")
        break  # Salir del bucle
    else:
        acum_notas += nota
        num_notas += 1