def main():
    emp = workers()
    tarifa = fares()


def fares():
    tarifa = int(input("Introduce la tarifa a la que se cobran las horas"))
    return tarifa


def workers():
    num_trabajadores = int(input("Introduce el Nº de trabajadores que tienes"))
    return num_trabajadores


def extra_hours():
    horas = int(input("Introduce las horas de los trabajadores, si las han tenido"))
    return horas


def salario_bruto(horas, num_trabajadores, tarifa):
    bruto = (horas * 1.5 + tarifa) + (38 * tarifa)
    return bruto


def tax_calc(bruto):
    tramo1 = (bruto - 600)
    tramo2 = (bruto - 1200)

    if bruto < 600:
        impuestos = 0
        return impuestos
    elif bruto < 1200:
        impuestos = tramo1 * 0.25 / 100
        return impuestos

    else:
        impuestos = tramo2 * 0.45 / 100
        return impuestos
