"""
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde
"""

renta = int(input("Introduce la renta del año pasado para calcular su tipo impositivo: "))

if renta < 10000:
    print("El tipo impositivo que te corresponde es del 5%")

elif 10000 > renta < 20000:
    print("El tipo impositivo que te corresponde es del 15%")

elif 20000 < renta < 35000:
    print("El tipo impositivo que te corresponde es del 20%")

elif 35000 < renta < 60000:
    print("El tipo impositivo que te corresponde es del 30%")

elif renta > 60000:
    print("El tipo impositivo que te corresponde es del 45%")
