# Muestra título en pantalla

print("=== GESTOR DE INVENTARIO ===")
# Creamos la lista principal para guardar la información de los productos
lista_productos = []
nombre_producto = ""
stock = 0
precio = 0
try:
    stop = True
    while stop:
        nombre_producto = input("Introduce el nombre del producto: ")
        continuar = input("Quieres continuar? (Y o N)").upper()
        if continuar == "N":  #Si introduce N termina el bucle
            stop = False
        elif continuar == "Y":
            print("Continuando...")
        else:
            print("La opcion que has introducido no es valida")

    # Lista de valores del producto actual
    stop = True
    while stop:
        stock = int(input("Cantidad en stock: "))
        continuar = input("Quieres continuar? (Y o N)").upper()
        if continuar == "N":  #Si introduce N termina el bucle
            stop = False
        elif continuar == "Y":
            print("Continuando...")
        else:
            print("La opcion que has introducido no es valida")
    stop = True
    while stop:
        precio = float(input("Precio por unidad (€): "))
        continuar = input("Quieres continuar? (Y o N)").upper()
        if continuar == "N":  #Si introduce N termina el bucle
            stop = False
        elif continuar == "Y":
            print("Continuando...")
        else:
            print("La opcion que has introducido no es valida")

    # Guardamos el alumno como diccionario solo si las variables tienen valor
    if stock > 0 and precio > 0 and nombre_producto != "":
        producto = {"nombre": nombre_producto, "cantidad": stock, "precio": precio}
        lista_productos.append(producto)
    else:
        print("Valores no validos detectados en la cantidad, precio Y/o nombre del producto")
except ValueError:
    print("⚠️ Por favor, introduce un número válido.")

acum_precio = 0
# Mostrar resultados finales
print("\n=== LISTADO INVENTARIO ===")
for i in lista_productos:
    print(f"{i['nombre']} {i['cantidad']} unidades x {i['precio']} = {i['cantidad'] * i['precio']}€")
    for j in lista_productos:
        acum_precio += j['cantidad'] * j['precio']
        print(f"Valor total del inventario {acum_precio}")
# Mensaje final
print("\n--- Fin del programa ---")
