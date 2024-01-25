"""
Realizar la carga de dos cadenas de caracteres. Indicar si son iguales o no y mostrarlas ordenadas
alfabéticamente
"""

cadena1 = str(input("Introduce la cadena 1"))

cadena2 = str(input("Introduce la cadena 1"))

if cadena1 == cadena2:
    print("Las cadenas que has introducido son iguales")

else:
    print("Las cadenas que has introducido no son iguales...")

print("Ordenar las cadenas alfabeticamente...")

if cadena1 < cadena2:
    print(cadena1)
    print(cadena2)
else:
    print(cadena2)
    print(cadena1)
