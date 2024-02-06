"""
Desarrollar un programa que permita almacenar los datos de n alumnos. Definir un diccionario
cuya clave será el número de alumno en el centro. Como valor almacenar una lista con el nombre, la
materia a la que está apuntado y la nota obtenida en dicha materia. Un alumno puede estar apuntado
a diferentes materias. Implementar funciones para cargar los datos de los alumnos, listar todos los
alumnos y consultar un alumno a través de su id. Una posible ejecución es:
"""


def cargar_dicc():
    diccionario = dict()
    continuar = True
    while continuar:
        clave = input("Ingrese el código del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        resp = "s"
        lista_materia_nota = []
        while resp == "s":
            materia = input("Ingrese el nombre de la materia: ")
            nota = int(input("Ingrese la nota: "))
            tupla = (materia, nota)
            lista_materia_nota.append(tupla)
            resp = input("Desea cargar otra materia [s/n]:")
        continuar = input("Desea cargar los datos de otro alumno [s/n]:")
        if continuar == "n":
            continuar = False
        diccionario[clave] = (nombre, lista_materia_nota)
    return diccionario


def listar_dicc(diccionario):
    for clave in diccionario:
        print("DNI del alumno: " + clave)
        print("Nombre del alumno: " + diccionario[clave][0])
        print("Materias y notas obtenidas: ")
        for materia, nota in diccionario[clave][1]:
            print(materia, " ", nota)


def buscar(diccionario):
    presente = False
    intro = input("Introduce el codigo del alumno para buscar: ")
    for palabra in diccionario:
        if palabra == intro:
            print("Los datos del alumno son: ", diccionario[intro])
            presente = True
    if not presente:
        print("No se ha encontrado el alumno")


def main():
    dicc = cargar_dicc()
    listar_dicc(dicc)
    buscar(dicc)


main()
