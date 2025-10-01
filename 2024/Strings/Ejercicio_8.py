"""
Ejercicio 8
Escribe un script que convierta un número entero decimal en binario utilizando
cadenas.
Análisis: Se divide el número por 2; si hay resto ponemos un 1: En caso
contrario 0 y nos detenemos cuando la división devuelva como resultado 0. El
resultado se almacena en una cadena. El resto se determina por el módulo %. Ten
en cuenta que trabjando con enteros, la división da siempre un entero truncado
El bloque principal puede ser:

def main():
numero = 255
print(numero, " en binario es ", decimal_binario(numero))
numero = 5
print(numero, " en binario es ", decimal_binario(numero))
main()
y su ejecución correcta:
/home/luis/PycharmProjects/Cadenas/venv/bin/python
/home/luis/PycharmProjects/Cadenas/PRACTICA-RESUELTA/pasar_binario.py
255 en binario es 11111111
5 en binario es 101
"""


def calculo_binario(numero):
    if numero < 2:
        return str(numero)
    else:
        return calculo_binario(numero // 2) + str(numero % 2)


def main():
    numero = 255
    print(numero, " en binario es ", calculo_binario(numero))
    numero = 4
    print(numero, " en binario es ", calculo_binario(numero))


main()
