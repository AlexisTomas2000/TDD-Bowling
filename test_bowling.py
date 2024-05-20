import Bowling

jugada = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1]

def test_Spare():
    jogo = Bowling.Juego()  # Corrección del nombre de la clase
    for tiro in jugada:
        jogo.Tirar(tiro)
    assert jogo.Score() == 29

