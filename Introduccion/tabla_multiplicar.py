"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10 separadas por
un tabulador “\t”.
"""

# Anidamos un for dentro de otro

for i in range(1, 10 + 1):
    multiplo = i
    print("\t")
    for x in range(1, 10 + 1):
        result = multiplo * x
        print(multiplo, "*", x, "=", result)
