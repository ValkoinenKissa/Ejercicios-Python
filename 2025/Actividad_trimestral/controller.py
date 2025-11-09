from pathlib import Path

from product import Product
from io_ops import IO

"""
Declaro una variable path donde instancio un objeto de la clase path, para pasarle
el path a todos los metodos que lo requieran, declaro esta variable duera de la clase para
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
        Controller.load_inventory()
        Controller.calculate_inventory_value()
        Controller.show_products_without_any_stock()

    # Incluyo una función para agregar más productos al fichero
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
        prices = IO.read_file_prices(path)
        acum = 0
        for i in prices:
            acum += i
        print(f"El valor total del inventario es de: {acum}€")

    @staticmethod
    def show_products_without_any_stock():
        product_list = IO.show_products_without_stock(path)
        if len(product_list) < 0:
            print("Actualmente no se han encontrado productos sin stock")

        else:
            print(f"Estos son los productos que actualmente no tienen stock: {product_list}")

    # TODO implementacion de metodo para actualizar el stock de un producto
