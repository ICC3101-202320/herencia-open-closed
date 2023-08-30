from print import Print

class PrintWithLog(Print):
    def __init__(self, str):
        super().__init__(str)

    def show(self):
        print('Ahora voy a imprimir el string')
        super().show()
        print('Terminé de imprimirlo')
        