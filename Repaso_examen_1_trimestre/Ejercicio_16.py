base = int(input("Introduce la base de tu triangulo de asteriscos: "))
altura = int(input("Introduce la altura de tu triangulo de asteriscos: "))


for j in range(altura):
    print()
    for i in range(base):
        print("*", end="")
