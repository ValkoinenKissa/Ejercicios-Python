"""
Realizar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivamente.
Después, imprimir los nombres y las notas de cada alumno
"""


def nombre_alumnos():
    nombre = []
    for i in range(0, 6):
        nombres_intro = str(input("Introduce el nombre de los alumnos: "))
        nombre.append(nombres_intro)
    return nombre


def nota_alumnos(nombre):
    nota = []
    for i in range(0, 6):
        datos_intro = int(input(f"Introduce la nota del alumno:  {nombre[i]}"))
        nota.append(datos_intro)
    return nota


def suspensos(nota):
    num_suspensos = 0
    for suspenso in nota:
        if suspenso < 5:
            num_suspensos += 1

    return num_suspensos


def imprime_resultados(nombre, nota):
    for i in range(5):
        print(nombre[i] + " " + str(nota[i]))


def main():
    nombre_de_alumnos = nombre_alumnos()
    nota_de_alumnos = nota_alumnos(nombre_de_alumnos)
    imprime_resultados(nombre_de_alumnos, nota_de_alumnos)

    cantidad_suspensos = suspensos(nota_de_alumnos)

    print(f"La cantidad de suspensos de la clase son: {cantidad_suspensos}")


main()
