from pathlib import Path


class IO:
    @staticmethod
    def read_file(path: Path):
        # with asegura que el archivo se cierre automáticamente, incluso si ocurre un error
        with open(path, "r") as file:  # La r indica a with que queremos leer el contenido
            content = file.read()
            print(content)

    @staticmethod
    def write_file(path: Path, write_string):
        with open(path, "a") as file: #La a índica que añadimos nuevo contenido al fichero sin sobreecribirlo
            file.write(write_string)

    @staticmethod
    def path_exits_false():
        print("El fichero no existe, creando fichero con contenido predeterminado...")
        with open("data/inventario.txt", "w") as file: #La w indica que sobreescribimos el fichero
            file.write("iPhone 15\n")
            file.write("900€ \n")
            file.write("20\n")

            file.write("Samsung S20\n")
            file.write("700€\n")
            file.write("0\n")

            file.write("Google pixel 3a\n")
            file.write("300€\n")
            file.write("10\n")
