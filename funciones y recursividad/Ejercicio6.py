def cacl_potencia(base, exponente):
    if exponente == 0:
        return 1

    return base * cacl_potencia(base, exponente - 1)


def main():
    base = int(input("Introduce la base: "))
    exponete = int(input("Introduce el exponente: "))
    print("El resultado de ", base, " elevado a ", exponete, "es ", cacl_potencia(base, exponete))


main()
