from pathlib import Path


class IO:
    @staticmethod
    def read_file(path: Path):
        # with asegura que el archivo se cierre automáticamente, incluso si ocurre un error
        with open(path, "r") as file:  # La r indica a with que queremos leer el contenido
            content = file.read()
            print(content)

    @staticmethod
    def read_file_prices(path: Path):
        prices = []

        with open(path, "r", encoding="utf-8") as file: #Utilizamos la codificación utf-8 para evitar fallos
            for line in file: #with genera un buffer de lectura que es almacenado en variable file
                #Iteramos esa variable file con un bucle for
                if line.startswith("Precio:"): #Con la función startswith detectamos la línea del archivo donde
                    #Se encuentra el tag Precio:
                    value = line.split(":")[1].strip() #Split divide la cadena en una lista,
                    # usando los dos puntos (:) como separador y strip elimina los espacios para que la conversion a
                    #entero no nos dé ningún fallo
                    prices.append(int(value)) #El valor se almacena en el array y se convierte de str a int

        return prices #Se devuelve el valor para usarlo en la clase controller

    @staticmethod
    def write_file(path: Path, write_string):
        with open(path, "a") as file: #La a índica que añadimos nuevo contenido al fichero sin sobreescribirlo
            file.write(write_string)

    @staticmethod
    def path_exits_false():
        print("El fichero no existe, creando fichero con contenido predeterminado...")
        with open("data/inventario.txt", "w") as file: #La w indica que sobreescribimos el fichero
            file.write("Nombre: iPhone 15\n")
            file.write("Precio: 900 \n")
            file.write("Stock: 20\n")

            file.write("Nombre: Samsung S20\n")
            file.write("Precio: 700\n")
            file.write("Stock: 0\n")

            file.write("Nombre: Google pixel 3a\n")
            file.write("Precio: 300\n")
            file.write("Stock: 10\n")
