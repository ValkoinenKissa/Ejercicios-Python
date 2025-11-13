from pathlib import Path

from product import Product
from io_ops import IO

"""
Declaro una variable path donde instancio un objeto de la clase path, para pasarle
el path a todos los metodos que lo requieran, declaro esta variable fuera de la clase para
hacerla global para todo el mismo fichero
"""
path = Path("data/inventario.txt")
# Array para almacenar objetos de la clase Producto
products = []


class Controller:

    def __init__(self):
        pass  # Constructor vacio

    @staticmethod
    def start_app():
        stop = False
        print("Bienvenido al programa de gestion de inventario, elige una opción: ")
        print("--------------------------------------------------------------------------------------------------")
        while not stop:
            print("1 - Carga del inventario, si el fichero no existe, se autogenerara un fichero de ejemplo")
            print("2 - Mostrar el inventario (Se imprime en pantalla el inventario mediante un formato legible")
            # Incluyo una función adicional para agregar más productos al fichero
            print("3 - Introducir un nuevo producto en el inventario (genera un nuevo producto en el fichero")
            print("4 - Calcular el valor total del inventario")
            print("5 - Identificar productos agotados (con stock igual a 0")
            print("6 - Actualizar cantidad de un producto (el producto debe de estar listado en el fichero)")
            print("7 - Abandonar el programa")
            print("--------------------------------------------------------------------------------------------------")
            option = str(input("Introduce la opción deseada (num opción) -> "))
            match option:
                case "1":
                    Controller.load_inventory()
                case "2":
                    Controller.load_inventory()
                case "3":
                    Controller.create_product()
                case "4":
                    Controller.calculate_inventory_value()
                case "5":
                    Controller.show_products_without_any_stock()
                case "6":
                    Controller.update_product_stock()
                case "7":
                    print("¡Hasta pronto!")
                    stop = True
                    # Default en python se escribe con un guion bajo _
                case _:
                    print(f"La opcion que has introducido: {option} no se corresponde a ninguna opcion \n"
                          f"listada en las opciones del programa, prueba de nuevo")

    @staticmethod
    def create_product():
        print("Usuario, introduce los datos del nuevo producto: ")
        product_name = str(input("Introduce el nombre del producto: "))
        price = str(input("Introduce el precio del producto: "))
        stock = str(input("Introduce el stock actual del producto: "))

        # Intancio el producto con los datos y lo meto en el array de productos:
        p = Product(product_name, price, stock)
        products.append(p)
        # los productos se cargan en el fichero de texto con este metodo:
        Controller.write_inventory()
        print("¡Producto añadido con éxito!")

    @staticmethod
    def load_inventory():
        if path.exists():
            # Le paso la instancia del objeto Path al metodo estatico de IO, internamente el metodo se lo pasa al with
            IO.read_file(path)

        else:
            # Este metodo de la clase IO crea un fichero con valores predefinidos
            IO.path_exits_false()

    @staticmethod
    def write_inventory():
        """
        Para escribir el fichero iteramos la lista de productos,
        llamamos al metodo toString e iteramos hasta la aparicion del caracter \n
        antes de ello llamamos al metodo IO.write_file para escribir el fichero con los datos
        """
        for p in products:
            IO.write_file(path, str(p))  # Se ejecuta la función to string sobre los productos almacenados en el array
            # de productos, y se pasa por parametro a la función write file que escribe la salida del str en el fichero txt
            if str(p) == "\n":
                break

    @staticmethod
    def calculate_inventory_value():
        prices = IO.read_file_prices(path) # Almacenamos la lista de precios y de stocks que hemos
        stocks = IO.read_file_stock(path) # generado en la clase controller
        acum = 0
        if len(prices) == len(stocks): #Comprobamos que cada precio de producto tenga un stock asignado
            for i in range(len(prices)):
                acum = acum + (prices[i] * stocks[i]) #Multiplicamos y sumamos al acumulador los precios y el stock
                # en cada iteracion del bucle
        else:
            print("Error: No se puede calcular el valor del inventario, revisa que el stock y el precio de \n"
                  "los productos no este incompleto dentro del fichero") #Si la longitud de los arrays es desigual
        print(f"El valor total del inventario es de: {acum}€") #Mostramos al usuario el valor total del inventario

    @staticmethod
    def show_products_without_any_stock():
        product_list = IO.show_products_without_stock(path)
        if len(product_list) == 0:
            print("Actualmente no se han encontrado productos sin stock")

        else:
            print(f"Estos son los productos que actualmente no tienen stock: {product_list}")

    @staticmethod
    def update_product_stock():
        IO.update_stock_by_product(path, 5, "iPhone 15")
