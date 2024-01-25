"""
Solicitar la carga por teclado de un string. Mostrar el total de caracteres del string y utilizar las
funciones explicadas anteriormente (upper, lower y capitalize).

"""

cadena_texto = str(input("Introduce una cadena"))

print(f"Total de caracteres del string: {len(cadena_texto)}")

cadena_minusculas = cadena_texto.lower()

print(cadena_minusculas)

cadena_capitalizada = cadena_texto.capitalize()

print(cadena_capitalizada)

cadena_minusculas = cadena_texto.upper()

print(cadena_minusculas)
