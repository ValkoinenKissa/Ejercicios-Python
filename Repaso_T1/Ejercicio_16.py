"""
16) Pide por teclado la altura y base de un rectángulo de asteriscos e imprímelo.
"""

base = int(input("Introduce la base que quieres que tenga el rectangulo: "))
print()
altura = int(input("Introduce la altura que quieres que tenga el rectangulo: "))

for i in range(0, base):
    print()
    for j in range(0, altura):
        print("*", end=" ")
