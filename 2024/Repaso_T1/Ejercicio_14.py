"""
Imprime por pantalla el menaje: desea continuar (s/n)?. Si la respuesta válida, es decir, una “n”
o una “s”, debe indicar el error y volver a solicitar la respuesta
"""

user_type = input("desea continuar (s/n)? ")
stop = False

while not stop:
    if user_type == "n" or user_type == "s":
        stop = True
    else:
        print("La respuesta introducida no es valida, por favor intentelo de nuevo")
        print()
        user_type = input("desea continuar (s/n)? ")
print()
print("Se esta instalando el .jar, por favor espere mientras tanto")
