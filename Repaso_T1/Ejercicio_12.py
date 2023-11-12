"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

password = str("contraseña")

user_intro = input("Usuario, introduce la contraseña a ver si logras adivinarla: ")

stop = False

while not stop:
    print("Vaya!! parace que no has conseguido adivinar la contraseña, sigue intentandolo: ")
    print()
    user_intro = input("Usuario, introduce la contraseña a ver si logras adivinarla: ")
    if user_intro == password:
        stop = True

print("Felicidades, has acertado la contraseña!!")
