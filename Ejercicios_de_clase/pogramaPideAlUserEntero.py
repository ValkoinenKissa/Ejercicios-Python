"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
los números impares desde 1 hasta ese número separados por comas.
"""
# Pedimos al usuario que introduzca un numero
num_entero = int(input("Introduce un numero positivo \n"))
"""Empezamos a contar en el 1, y al numero que introduce el usuario le sumamos uno, ya que python cuenta hasta el num
anterior"""
for i in range(1, num_entero + 1, 2):
    # Imprimimos por pantalla la variable contadora del bucle
    print(i, end=",")

num = int(input("Introduce otro numero: \n"))

print("Los numeros impares hasta numero", num, "son")
for i in range(1, num+1):
    if i % 2 != 0:
        print(i, end=",")
