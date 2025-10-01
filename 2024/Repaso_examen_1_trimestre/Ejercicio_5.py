def intro_num():
    num = int(input("Introduce un numero para calcular su factorial: "))
    return num


def factorial(num):
    if num == 0:
        return 1

    else:
        return num * factorial(num - 1)


def main():
    num = intro_num()
    factorial_num = factorial(num)
    print(f"El factorial de {num} es {factorial_num}")


main()
