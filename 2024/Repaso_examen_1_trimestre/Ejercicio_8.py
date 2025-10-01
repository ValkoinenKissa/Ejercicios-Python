def intro_num():
    num = int(input("Introduce un numero para convertirlo en binario: "))
    return num



def conversion_binaria(num):
    if num < 2:
        return str(num)

    else:
        return conversion_binaria(num//2) + str(num % 2)


def main():
    numero_entrada = intro_num()
    conversion = conversion_binaria(numero_entrada)
    print(f"El resultado de la conversion binaria es: {conversion}")

main()
