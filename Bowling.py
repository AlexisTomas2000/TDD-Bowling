class Juego:
    def __init__(self):
        self.puntos = 0
        self.jugada = []

    def Tirar(self, pinos: int):
        self.jugada.append(pinos)

    def Score(self):
        total = sum(self.jugada)
        if len(self.jugada) >= 2:
            ultimo_tiro = self.jugada[-2]
            penultimo_tiro = self.jugada[-3] if len(self.jugada) >= 3 else 0
            if ultimo_tiro + penultimo_tiro == 10:
                total += self.jugada[-1]
        return total
