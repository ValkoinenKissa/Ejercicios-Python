def intro_base():
    base = int(input("Introduce la base: "))
    return base


def intro_exponente():
    exponente = int(input("Intro exponenete: "))
    return exponente


def cal_potencia(base, exponente):
    if exponente == 0:
        return 1

    else:
        return base * cal_potencia(base, exponente-1)


def main():
    base = intro_base()
    exponente = intro_exponente()
    potencia = cal_potencia(base, exponente)
    print(f"La potencia de {base} elevado a {exponente} es {potencia}")


main()