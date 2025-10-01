# Introduce por teclado dos variables de tipo entero,
# calcula su suma e imprime el resultado en
# pantalla.

variable_1 = int(input("Introduce un valor"))
variable_2 = int(input("Introduce otro valor"))

resultado = variable_1 + variable_2
print("El resultado de la suma es:", resultado)

# Introduce por teclado dos e imprime cual es menor.

numero_1 = int(input("Introduce un numero para calcular cual es el menor"))
numero_2 = int(input("Introduce otro numero"))

if numero_1 < numero_2:
    print(numero_1)
else:
    print("El numero menor que has introducido es el:", numero_2)

# Introduce por teclado un número e imprime en pantalla si es negativo, 0 o positivo.
