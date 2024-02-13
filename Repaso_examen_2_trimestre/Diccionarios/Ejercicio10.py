"""
Crear una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista, modificar
sus datos y volver a convertir a tupla. (Para convertir a tupla utilizaríamos la función tuple() y para
convertir en lista la función list()).
"""

nueva_tupla = (1, 5, 7)

nueva_lista = list(nueva_tupla)

print(nueva_lista)

otra_vez_tupla = tuple(nueva_lista)

print(otra_vez_tupla)
