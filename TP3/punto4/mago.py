from random import*
from personaje import Personaje

class Mago(Personaje):
    def __init__(self, vida, nivelAtaque, nivelDefensa):
        super().__init__(vida, nivelAtaque, nivelDefensa)
        self._nombre = "Mago valdivia"

    def atacar(self):
        print("El", self._nombre, "realizo un ataque", )
        if randint(0,1) == 1:
            print("¡¡¡Golpe critico!!!")
            self._nivelAtaque *= 5
        return super().atacar()

    def defender(self, danio):
        if randint(0,1) == 1:
            print("¡¡¡El", self._nombre, "recibio un aura de proteccion!!!")
            self._nivelDefensa *= 5
        if danio > self._nivelDefensa:
            self._vida -= (danio - self._nivelDefensa)
            self._nivelDefensa -= danio
            print("¡¡El ataque rompio el hechizo de proteccion!!")
            self._nivelDefensa = 0
            if not super().vivo():
                print("El", self._nombre, "ha muerto")
            else:
                print("El nivel de vida del",self._nombre," es de:",self._vida)
        else:
            self._nivelDefensa -= danio
            print("El nivel de defensa del",self._nombre,"es de", self._nivelDefensa)