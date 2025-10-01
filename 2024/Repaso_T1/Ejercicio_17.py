"""
17) Pide por teclado la altura o base de un triángulo como éste:
*
**
***
"""

altura = int(input("Introduce la altura que quieres que tenga el triangulo: "))

for i in range(0, altura + 1):
    print()
    for j in range(0, i):
        print("*", end=" ")
