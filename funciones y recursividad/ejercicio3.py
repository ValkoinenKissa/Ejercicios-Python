def calculo_potencia(base, exponete):
    acum = 1
    for i in range(1, exponete+1):
        acum *= base
    return acum


def main():
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))
    print("El resultado de la potencia es:", calculo_potencia(base, exponente))


main()
