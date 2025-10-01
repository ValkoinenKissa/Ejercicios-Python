"""
Diseña una función que calcule y retorne la potencia de una base entera positiva elevada a un
exponente entero positivo. Ejemplo: 2 ** 0 = 1, 2**3 = 8
"""


def intro_base():
    num_base = int(input("Introduce una base: "))
    return num_base


def intro_exponente():
    num_exponenete = int(input("Introduce un exponenete: "))
    return num_exponenete


def calc_potencia(num_base, num_exponente):
    if num_exponente <= 0:
        return 1

    else:
        return num_base * calc_potencia(num_base, num_exponente - 1)


def imprime_results(num_base, num_exponenete, result):
    print(f"La potencia de {num_base} elevada a {num_exponenete} es {result}")


def main():
    base = intro_base()
    exponente = intro_exponente()
    potencia = calc_potencia(base, exponente)
    imprime_results(base, exponente, potencia)


main()
