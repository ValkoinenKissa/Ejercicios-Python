"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10 separadas por
un tabulador “\t”.
"""

for i in range(1, 10+1):
    print()
    for j in range(0,10+1):
        print(f"{i} * {j} = {i * j}")