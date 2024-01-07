"""
Imprime por pantalla el menaje: desea continuar (s/n)?. Si la respuesta válida, es decir, una “n”
o una “s”, debe indicar el error y volver a solicitar la respuesta
"""

introDatos = input("desea continuar (s/n)? ")


while introDatos != "s" and introDatos != "n":
    introDatos = input("Respuesta incorrecta, desea continuar (s/n)?")

print("Ejecución finalizada con exito")
