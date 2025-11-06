from inventory_management import Product

class Controller:

    def __init__(self):
        pass #Constructor vacio

    @staticmethod
    def start_app():
        p = Product("default", 0, 0)
        p.load_inventory()



    def create_product(self):
        print("Usuario, introduce los datos del nuevo producto: ")
        #TODO Implementar este metodo
