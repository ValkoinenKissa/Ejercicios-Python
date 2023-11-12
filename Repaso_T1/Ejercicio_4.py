"""
Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
Para convertir la cadena a minúsculas se hace: password.lower()
"""

password = "Pastel-de-fresas"
stop = True

usuario_escribe = input("Usuario, introduce la contraseña para acceder a tu cuenta: ")

if usuario_escribe != password:
    stop = False

while not stop:
    usuario_escribe = input("La contraseña que has introducido es incorrecta, por favor prueba de nuevo: ")
    if usuario_escribe == password:
        stop = True

print("Has iniciado la sesion correctamente")
