def factorial(num):
    acum = 1
    for i in range(1, num+1):
        acum = acum * i

    return acum


def main():
    num = int(input("Introduce un numero: "))
    print("El resultado es: ", factorial(num))


main()
