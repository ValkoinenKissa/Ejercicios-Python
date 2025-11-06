from pathlib import Path
from io_ops import IO

"""
Declaro una variable path donde instancio un objeto de la clase path, para pasarle
el path a todos los metodos que lo requieran, declaro esta variable duera de la clase para
hacerla global para todo el mismo fichero
"""
path = Path("data/inventario.txt")


class Product:
    # Este es el constructor del producto, con tres atributos, el self es equivalente al this de Java
    def __init__(self, product_name, price_eur, avalible_stock):
        self.product_name = product_name
        self.price_eur = price_eur
        self.avalible_stock = avalible_stock

    # Sobreescritura del metodo str que es equivalente al toString de java
    def __str__(self):
        return (f"Nombre del producto: {self.product_name} \n"
                f"Precio del producto: {self.price_eur}€ \n"
                f"Cantidad disponible en stock: {self.avalible_stock} \n")

    # carga de inventario, metodo para leer fichero texto
    def load_inventory(self):
        if path.exists():
            # Le paso la instancia del objeto Path al metodo estatico de IO, internamente el metodo se lo pasa al with
            IO.read_file(path)

        else:
            IO.path_exits_false()

    #Incluyo una funcion para agregar mas productos al fichero
    def write_inventory(self):
        IO.write_file(path, self.product_name)
        IO.write_file(path, self.price_eur)
        IO.write_file(path, self.avalible_stock)
