def intro_base():
    base = int(input("introduce la base: "))
    return base


def intro_exponente():
    exponente = int(input("introduce la base: "))
    return exponente


def cacl_potencia(base, exponete):
    acum = 1
    for i in range(1, exponete + 1):
        acum *= base

    return acum


def imprime_resultados(acum):
    print(f"El resultado de la potencia es {acum}")


def main():
    base = intro_base()
    exponente = intro_exponente()
    potencia = cacl_potencia(base, exponente)
    imprime_resultados(potencia)


main()
