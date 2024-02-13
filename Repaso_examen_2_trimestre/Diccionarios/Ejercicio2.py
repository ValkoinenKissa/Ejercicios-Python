print("Introduce el nombre de los alumnos y sus notas: ")

nombre_alumnos = []

nota_alumnos = []

for i in range(5):
    nombre_alumnos.append(input("Nombre del alumno: "))
    nota_alumnos.append(input("Introduce la nota del alumno: "))

for i in range(len(nombre_alumnos)):
    print(nombre_alumnos[i], "-->", nota_alumnos[i])
