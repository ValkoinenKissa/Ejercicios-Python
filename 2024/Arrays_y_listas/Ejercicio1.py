"""
Escribe las siguientes sentencias:
declaramos una lista vacia.
creamos un bucle para escribir cada elemento de la lista
una vez rellenado el lista, lo imprimimos
obtener la longitud del lista

"""
lista_vacia = []
contador = 5

for i in range(0, 5):
    lista_vacia.append(input("Escribe lo que quieras: "))
    print("Registro actualizado, espacio restante: ", contador, " espacios")
    contador -= 1

longitud_lista = lista_vacia
print("Aqui se imprime la lista")
print(longitud_lista)

print("Aqui se imprime la longitud de la lista: ")
print(len(longitud_lista))
