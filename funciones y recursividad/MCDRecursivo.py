def mcd_recursivo(num1, num2):
    if num1 == num2:
        return num1

    elif num1 > num2:
        return mcd_recursivo(num1 - num2, num2)

    elif num1 < num2:
        return mcd_recursivo(num1, num2 - num1)


def main():
    print("Este es un programa para calcular el mcd de un numero")
    num1 = int(input("Introduce el num1: "))
    num2 = int(input("Introduce el num2: "))
    print("El mcm es:", mcd_recursivo(num1, num2))


main()
