"""
Crear un diccionario que defina como clave el número de dni de una persona y como valor un
string con el nombre. Cargar los datos de 4 personas, listar el diccionario completo y realizar una
tercera función para consultar el nombre de la persona introduciendo su dni
"""


def cargar_datos(diccionario):
    for i in range(4):
        dni = input("Introduce el DNI de la persona: ")
        nombre = input("Introduce el nombre de la persona: ")
        diccionario[dni] = nombre

    return diccionario


def listar_diccionario(diccionario):
    for dni, nombre in diccionario.items():
        print(dni, " --> ", nombre)


def busqueda(diccionario):
    dni_consulta = input("Introduce el dni para buscar a la persona: ")
    encontrado = False
    nombre_persona = None

    for dni in diccionario.keys():
        if dni_consulta == dni:
            encontrado = True
            nombre_persona = diccionario[dni]

    if encontrado:
        print(f"El dni introducido {dni_consulta} perternece a {nombre_persona}")

    else:
        print("El documento introducido no pertenece a nadie...")


def main():
    diccionario = {}
    datos_personas = cargar_datos(diccionario)
    listar_diccionario(datos_personas)
    opcion = input("Introduce una S si quieres buscar a una persona, de lo contrario, introduce una N")
    if opcion.upper() == "S":
        busqueda(datos_personas)

    else:
        print("Hata pronto!!")


main()
