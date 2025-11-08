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
            IO.write_file(path, str(p))
            if str(p) == "\n":
                break

    @staticmethod
    def calculate_inventory_value():
        prices = IO.read_file_prices(path)
        acum = 0
        for i in prices:
            acum += i
        print(f"El valor total del inventario es de: {acum}€")


    # TODO Implementacion metodo para mostrar los prodcutos agotados stock:0

    # TODO implementacion de metodo para mostar los productos que estan agotados
