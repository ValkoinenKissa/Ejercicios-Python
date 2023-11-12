# 3) Introduce por teclado un número e imprime en pantalla si es negativo, 0 o positivo.

num = int(input("Introduce un numero entero: "))

if(num > 0):
    print("El numero que has introducido es positivo")

elif(num < 0):
    print("El numero que has introducido es negativo")

else:
    print("El numero que has introducido es 0")
