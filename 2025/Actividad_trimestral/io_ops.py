from pathlib import Path

class IO:
    # El decorador @staticmethod nos sirve para declararle al intérprete que un metodo es estatico y no requiere de una
    # instancia de clase
    @staticmethod
    def read_file(path: Path):
        # with asegura que el archivo se cierre automáticamente, incluso si ocurre un error
        with open(path, "r") as file:  # La r indica a with que queremos leer el contenido
            content = file.read()
            print(content)

    @staticmethod
    def read_file_prices(path: Path):
        prices = []

        with open(path, "r", encoding="utf-8") as file:  # Utilizamos la codificación utf-8 para evitar fallos
            for line in file:  # with genera un buffer de lectura que es almacenado en variable file
                # Iteramos esa variable file con un bucle for
                if line.startswith("Precio:"):  # Con la función startswith detectamos la línea del archivo donde
                    # Se encuentra el tag Precio:
                    value = line.split(":")[1].strip()  # Split divide la cadena en una lista,
                    # usando los dos puntos (:) como separador y strip elimina los espacios para que la conversion a
                    # entero no nos dé ningún fallo
                    prices.append(int(value))  # El valor se almacena en el array y se convierte de str a int

        return prices  # Se devuelve el valor para usarlo en la clase controller

    @staticmethod
    def show_products_without_stock(path: Path):
        products_stock = []
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines() #Leemos el archivo entero
            """
            enumerate() es una función integrada de Python que sirve para recorrer una secuencia (lista, tupla, etc.)
             obteniendo a la vez el índice y el valor de cada elemento.
            """
            for i, line in enumerate(lines):
                """
                i es el número de línea (0, 1, 2, …).
                line es el contenido de esa línea.
                """
                if line.startswith("Stock:"): #Aquí se comprueba que la línea comience con Stock: si no se ignora y
                    #Se pasa a la siguiente
                    value = int(line.split(":")[1].strip()) #Dividimos en dos la cadena, limpiamos espacios
                    # y pasamos el stock a entero para evaluarlo
                    if value == 0: #Si el stock es 0 se entra en el bucle anidado
                        for j in range(i -1, -1, -1):
                            """
                            i-1 -> start -> -1 stop, -> -1 step
                            
                            i - 1 → empieza justo una línea antes de la línea Stock:,
                            porque queremos mirar hacia atrás (el nombre siempre está antes del stock).
                            En el ejemplo: i = 5, así que empezamos en 4.
                            
                            -1 (segundo parámetro) → es el límite final ya que 0 correspondería a la primera linea del
                            archivo. Ej, en el archivo generado automáticamente si pusiéramos el stop = 0 correspondería
                            a Nombre: Iphone 15 y no al final del archivo
                            
                            -1 (tercer parámetro) → es el paso, el incremento (en este caso decremento).
                            Como es negativo, el bucle va hacia atrás: 4, 3, 2, 1, 0.
                            """
                            if lines[j].startswith("Nombre:"): #Se comprueba que la linea del la posicion del indice J
                                #Sea == a Nombre: y se realiza la extraccion del nombre de los productos
                                product = lines[j].split(":")[1].strip()
                                products_stock.append(product)
                                #Se rompe el bucle por si hay que seguir evaluando más stocks que sean igual a 0
                                break
        return products_stock  # Se devuelve el valor para usarlo en la clase controller

    @staticmethod
    def update_stock_by_product(path: Path, new_stock, product):
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if f"Nombre: {product}" in line:
                    # El stock está 2 líneas más abajo según el formato del archivo
                    stock_line_index = i + 2
                    lines[stock_line_index] = f"Stock: {new_stock}\n"
                    break  # salimos una vez hecho el cambio
                else:
                    print("El producto introducido no se encuentra en el fichero por favor, revisa que los \n"
                          "espacios, mayúsculas y minúsculas del valor introducido correspondan dentro del fichero")
        with open(path, "w", encoding="utf-8") as new_file:
            new_file.writelines(lines)
            print("El stock ha sido actualizado correctamente")


    @staticmethod
    def write_file(path: Path, write_string):
        with open(path, "a") as file:  # La a índica que añadimos nuevo contenido al fichero sin sobreescribirlo
            file.write(write_string)

    @staticmethod
    def path_exits_false():
        print("El fichero no existe, creando fichero con contenido predeterminado...")
        with open("data/inventario.txt", "w") as file:  # La w indica que sobreescribimos el fichero
            file.write("Nombre: iPhone 15\n")
            file.write("Precio: 900 \n")
            file.write("Stock: 20\n")

            file.write("Nombre: Samsung S20\n")
            file.write("Precio: 700\n")
            file.write("Stock: 0\n")

            file.write("Nombre: Google pixel 3a\n")
            file.write("Precio: 300\n")
            file.write("Stock: 10\n")
