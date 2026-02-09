class Product:
    # Este es el constructor del producto, con tres atributos, el self es equivalente al this de Java
    def __init__(self, product_name, price_eur, avalible_stock):
        self.product_name = product_name
        self.price_eur = price_eur
        self.avalible_stock = avalible_stock

    # Sobreescritura del metodo str que es equivalente al toString de java
    def __str__(self):
        #La forma de etiquetar el output del toString será clave para luego ejecutar metodos de lectura sobre el fichero
        return (f"Nombre: {self.product_name}\n"
                f"Precio: {self.price_eur}\n"
                f"Stock: {self.avalible_stock}\n")