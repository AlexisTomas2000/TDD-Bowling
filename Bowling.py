class Juego():
    pass
    def __init__(self) -> None:
        self.puntos = 0
        self.jugada = []

    def Tirar(self,pinos:int):
        self.jugada.append(pinos)

    def Score(self):
        total = sum(self.jugada)
        ultimo_tiro = self.jugada[len(self.jugada)-2]
        penultimo_tiro = self.jugada[len(self.jugada)-3]
        if ultimo_tiro + penultimo_tiro == 10:
                total += self.jugada[len(self.jugada)-1]
        return total
