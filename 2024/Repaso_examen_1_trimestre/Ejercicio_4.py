def intro_num1():
    num1 = int(input("Introduce el primer numero: "))
    return num1


def intro_num2():
    num2 = int(input("Introduce el primer numero: "))
    return num2


def calc_mcd(num1, num2):
    if num1 == num2:
        return 1

    else:
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1

        return num1


def main():
    num1 = intro_num1()
    num2 = intro_num2()
    calc_mcd(num1, num2)
    print("El resultado es: ", calc_mcd(num1, num2))


main()
