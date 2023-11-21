altura = int(input("Introduce la altura de tu triangulo de asteriscos: "))

for i in range(altura):
    print()
    for j in range(i):
        print("*", end="")