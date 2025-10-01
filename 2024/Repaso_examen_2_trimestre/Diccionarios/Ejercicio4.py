"""
Una empresa divide el trabajo en dos turnos (mañana y tarde) en las que trabajan 6 empleados (3/
turno). Agrupar los sueldos de los empleados en dos listas y mostrar después las listas por consola

"""

turno_manana = []
for i in range(3):
    turno_manana.append(input("Introduce los salarios del turno de mañana: "))

turno_tarde = []
for i in range(3):
    turno_tarde.append(input("Introduce los salarios del turno de tarde: "))


print("Salarios turno tarde: ")
print(turno_tarde)
print("Salarios turno mañana: ")
print(turno_manana)
