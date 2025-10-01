class ControlVolumen:
    def __init__(self):
        self.subir = 0
        self.bajar = 0
        self.vol = 0

    def encender(self):
        self.vol = 3
        print("Encendiendo el mp3")
        print("El volumen actual es de: ", self.vol)

    def boton_bajar(self):
        self.vol -= 1
        if self.vol < 0:
            self.vol = 0
        print("El volumen actual es de: ", self.vol)

    def boton_subir(self):
        self.vol += 1
        if self.vol > 10:
            self.vol = 10
        print("El volumen actual es de: ", self.vol)

    def silenciar(self):
        self.vol = 0
        print("El volumen actual es de: ", self.vol)


def main():
    mp3 = ControlVolumen()
    mp3.encender()
    mp3.boton_subir()
    mp3.boton_subir()
    mp3.boton_bajar()


main()
