"""
Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
Para convertir la cadena a minúsculas se hace: password.lower()
"""

password = "iesgoya"

validate = input("Introduce la contraseña").lower()

while password != validate:
    print("Lo siento, la contraseña que has introducido no es correcta"
          "vuelve a intentarlo")
    validate = input("Introduce la contraseña").lower()

print("Has iniciado sesion correctamente")
