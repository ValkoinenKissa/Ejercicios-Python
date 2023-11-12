"""
Escribir un programa que pida al usuario dos números float y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

print("Introduce dos numeros decimales \n")

dividendo = float(input("Introduce el primer valor: "))
divisor = float(input("Introduce el segundo valor: "))

try:
    resultado = dividendo/divisor
    print("El resultado de tu division es: ", resultado)

except ZeroDivisionError:
    print("No puedes dividir un numero entre 0, no "
          "lo intentes o la maquina explotara")
