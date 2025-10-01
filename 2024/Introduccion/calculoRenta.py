"""
Calculo de renta, Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde.
"""

renta = int(input("Introduce tu renta para calcular el tipo impositivo que "
                  "te corresponda: \n"))
tipo_impositivo = 0

if renta <= 10000:
    tipo_impositivo = 5

elif renta >= 10000 and renta <= 20000:
    tipo_impositivo = 15

elif renta >= 20000 and renta <= 35000:
    tipo_impositivo = 20

elif renta >= 35000 and renta <= 60000:
    tipo_impositivo = 30

elif renta >= 60000:
    tipo_impositivo = 45

print("En funcion a tu renta que son", renta, "$ el tipo impositivo que te corresponde pagar son:", tipo_impositivo, "%")
