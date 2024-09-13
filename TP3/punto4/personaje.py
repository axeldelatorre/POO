from abc import ABC, abstractmethod
class Personaje():
    def __init__(self, vida, nivelAtaque, nivelDefensa):
        self._vida = vida = 100
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa

    def atacar(self):
        print("El ataque hizo", self._nivelAtaque, "de daño")
        return self._nivelAtaque

    def defender(self, atacar):
        pass
        
    def vivo(self):
        if self._vida  > 0:
            return self._vida