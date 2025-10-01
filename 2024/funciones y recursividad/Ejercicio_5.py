def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = int(input("Introduce un numero para calcular su factorial: "))
    print("El factorial es ", factorial(n))


main()
