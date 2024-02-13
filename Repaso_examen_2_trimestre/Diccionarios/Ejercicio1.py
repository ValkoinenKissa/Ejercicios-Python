lista_vacia = []
stop = False

for x in range(5):
    lista_vacia.append((input("Ingresea valores para la lista: ")))

for i in lista_vacia:
    print(i)

print("La longitud de la lista es: ", len(lista_vacia))
