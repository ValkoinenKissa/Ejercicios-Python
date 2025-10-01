def intro_numero():
    return int(input("Introduce un numero para calcular su binario: "))


def calculo_binario(numero):
    if numero < 2:
        return str(numero)
    else:
        return calculo_binario(numero // 2) + str(numero % 2)


def main():
    numero = intro_numero()
    binario = calculo_binario(numero)
    print(binario)


main()
