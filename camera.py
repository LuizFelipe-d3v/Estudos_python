class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Ja esta filmando...')
            return
        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NAO esta filmando...')
            return
        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Nao pode fotografar filmando...')
            return
        
        print(f'{self.nome} esta fotografando...')



c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c1.fotografar)  
# print(c2.filmando)