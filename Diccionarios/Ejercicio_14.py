"""
Desarrollar un programa que permita almacenar los datos de n alumnos. Definir un diccionario
cuya clave será el número de alumno en el centro. Como valor almacenar una lista con el nombre, la
materia a la que está apuntado y la nota obtenida en dicha materia. Un alumno puede estar apuntado
a diferentes materias. Implementar funciones para cargar los datos de los alumnos, listar todos los
alumnos y consultar un alumno a través de su id. Una posible ejecución es:
"""


def pedir_datos():
    alumnos = []
    stop = False
    while not stop:
        alumnos = dict()
        codigo = int(input("Ingrese el codigo del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        materia = input("Ingrese el nombre de la materia: ")
        nota = int(input("Ingrese la nota: "))
