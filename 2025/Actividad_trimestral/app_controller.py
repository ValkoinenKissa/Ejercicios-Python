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


def format_output(): #Metodo para mostrar esta linea separadora por pantalla
    print("--------------------------------------------------------------------------------------------------")


class AppController:

    def __init__(self):
        pass  # Constructor vacio

    @staticmethod
    def start_app():
        stop = False
        print("Bienvenido al programa de gestion de inventario, elige una opción: ")
        format_output()
        while not stop:
            print("1 - Carga del inventario, si el fichero no existe, se autogenerara un fichero de ejemplo")
            print("2 - Mostrar el inventario (Se imprime en pantalla el inventario mediante un formato legible")
            # Incluyo una función adicional para agregar más productos al fichero
            print("3 - Introducir un nuevo producto en el inventario (genera un nuevo producto en el fichero")
            print("4 - Calcular el valor total del inventario")
            print("5 - Identificar productos agotados (con stock igual a 0")
            print("6 - Actualizar cantidad de un producto (el producto debe de estar listado en el fichero)")
            print("7 - Abandonar el programa")
            format_output()
            option = str(input("Introduce la opción deseada (num opción) -> "))
            match option:
                case "1":
                    AppController.load_inventory()
                case "2":
                    AppController.load_inventory()
                case "3":
                    AppController.create_product()
                case "4":
                    AppController.calculate_inventory_value()
                case "5":
                    AppController.show_products_without_any_stock()
                case "6":
                    AppController.update_product_stock()
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
        AppController.write_inventory()
        format_output()
        print("¡Producto añadido con éxito!")
        format_output()
    @staticmethod
    def load_inventory():
        if path.exists():
            # Le paso la instancia del objeto Path al metodo estatico de IO, internamente el metodo se lo pasa al with
            IO.read_file(path)
            format_output()
            print("El inventario ha sido cargado con exito")
            format_output()

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
            format_output()
            print("Error: No se puede calcular el valor del inventario, revisa que el stock y el precio de \n"
                  "los productos no este incompleto dentro del fichero") #Si la longitud de los arrays es desigual
            format_output()
        format_output()
        print(f"El valor total del inventario es de: {acum}€") #Mostramos al usuario el valor total del inventario
        format_output()
    @staticmethod
    def show_products_without_any_stock():
        product_list = IO.show_products_without_stock(path)
        if len(product_list) == 0:
            format_output()
            print("Actualmente no se han encontrado productos sin stock")
            format_output()

        else:
            format_output()
            print(f"Estos son los productos que actualmente no tienen stock: {product_list}")
            format_output()

    @staticmethod
    def update_product_stock():
        product_name =str(input("Introduce el nombre del producto el cual quieres modificar su stock: "))
        product_new_stock = int(input("Introduce el nuevo stock del producto: "))
        IO.update_stock_by_product(path, product_new_stock, product_name)
