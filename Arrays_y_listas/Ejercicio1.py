"""
Escribe las siguientes sentencias:
declaramos una lista vacia.
creamos un bucle para escribir cada elemento de la lista
una vez rellenado el lista, lo imprimimos
obtener la longitud del lista

"""
lista_vacia = []

for i in range(0, 11):
    lista_vacia.append(input("Escribe lo que quieras"))

lista_con_datos = lista_vacia
print("Aqui se imprime la lista")
print(lista_con_datos)

print("Aqui se imprime la longitud de la lista: ")
print(len(lista_con_datos))
