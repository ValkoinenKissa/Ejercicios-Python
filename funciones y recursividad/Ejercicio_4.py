def calculo_mcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2

        else:
            num2 = num2 - num1
    return num1


def main():
    num1 = int(input("Introduce el numero 1 para calcular el mcd: "))
    num2 = int(input("Introduce el numero 2 para calcular el mcd: "))
    print("El mcm de los numeros que has introducido es: ", calculo_mcd(num1, num2))


main()
