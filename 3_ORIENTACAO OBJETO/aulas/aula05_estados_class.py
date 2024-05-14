#Mantendo estados dentro da calsse

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Ja esta Filmando')
            return

        self.filmando = True
        print(f'{self.nome} esta Filmando...')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Nao pode fotografar Filmando!')
            return
        print(f'{self.nome} esta Fotografando!')

    def parar_filmar(self):
        if self.filmando:
            print(f'{self.nome} paraou de Filmar')
            self.filmando = False


camera1 = Camera('Sony')
camera2 = Camera('Cannon')

camera1.filmar()
camera2.filmar()
camera1.filmar()
camera2.filmar()
camera1.fotografar()
camera2.fotografar()
camera1.parar_filmar()
camera2.parar_filmar()
camera1.fotografar()
camera2.fotografar()
print()
print()
# print(camera1.filmando)
# print(camera2.filmando)
