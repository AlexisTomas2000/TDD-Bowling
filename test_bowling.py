from Bowling import *
jugada = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,1,1]
def test_Spare():
    jogo = Juego()
    for tiro in jugada:
        jogo.Tirar(tiro)
    assert jogo.Score()==29


"""def test_1():
    jogo = Juego()
    for tiro in range(20):
        jogo.Tirar(1)
    assert jogo.Score()==20"""

"""def test_lose():
    jogo = Juego()
    for tiro in range(20):
        jogo.Tirar(0)
    assert jogo.Score()==0"""