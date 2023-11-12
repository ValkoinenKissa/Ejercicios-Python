"""
Diseña una función que calcule y retorne la potencia de una base entera positiva elevada a un
exponente entero positivo. Ejemplo: 2 ** 3 = 8 , 2 ** 0 = 1
"""


def intro_base():
    base = int(input("Introduce la base: "))
    return base


def intro_exponente():
    exponenete = int(input("Introduce el exponenete: "))
    return exponenete


def calculo_potencia(base, exponente):
    acum = 1
    for i in range(1, exponente + 1):
        acum *= base

    return acum


def muestra_resultados(base, exponente, acum):
    print(f"La base {base} elevada al exponenete {exponente} es {acum}")


def main():
    base = intro_base()
    exponente = intro_exponente()
    calculo = calculo_potencia(base, exponente)
    muestra_resultados(base, exponente, calculo)


main()
