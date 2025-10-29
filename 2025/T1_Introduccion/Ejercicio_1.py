#solicitud de datos al usuario
print("Usuario, introduce tres numeros enteros \n")

try:
    #a la funcion input se declara que solo debe de aceptar enteros
    num1 = int(input("Introduce el primer numero: "))
    print(f"Has introducido el numero {num1} y su tipo de dato es: {type(num1)}")
    num2 = int(input("Introduce el segundo numero: "))
    print(f"Has introducido el numero {num2} y su tipo de dato es: {type(num2)}")
    num3 = int(input("Introduce el tercer numero: "))
    print(f"Has introducido el numero {num3} y su tipo de dato es: {type(num3)}")

    # parte de calculo
    array_numeros = [num1, num2, num3]

    print(f"De los numeros introducidos el menor es: {min(array_numeros)}")
    print(f"De los numeros introducidos el mayor es: {max(array_numeros)}")

    suma = num1+num2+num3
    resta = num1-num2-num3
    producto = num1*num2*num3
    cociente_real = suma/3
    division_entera = suma//3
    resto = suma%3
    potencia =  max(array_numeros) ** min(array_numeros)

    print(f"La suma de los tres numeros es: {suma}")
    print(f"La resta secuencial de los tres numneros es: {resta}")
    print(f"El producto de los tres numneros es: {producto}")
    print(f"El cociente real de los tres numneros es: {cociente_real}")
    print(f"La division entera de los tres numneros es: {division_entera}")
    print(f"El resto de la division de los tres numneros es: {resto}")
    print(f"La potencia del mayor elevado al menor es: {potencia}")

    print(f"La media aritmetica expresada como numero entero es: {int(cociente_real)}")
    print(f"La suma como texto es: {str(suma)}")

    if suma % 2 == 0:
        print("La suma es par")
    else:
        print("La suma es impar")

    if cociente_real < 10:
        print("La media es menor que 10")
    elif cociente_real == 10:
        print("La media es 10")
    else:
        print("La media es mayor que 10")

 #Si se introduce otro tipo de dato se genera una excepcion y se controla aqui
except ValueError:
    print("ERROR: El numero introducido no es entero o no has introducido ningun numero")


