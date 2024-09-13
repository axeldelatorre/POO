from random import*
from carta import Carta

class Especial(Carta):
    def __init__(self,nombre, club, pais, habilidadEspecial, quimica):
        super().__init__(nombre, club, pais, habilidadEspecial, quimica)
        self._habilidadEspecial = ["Ataque", "Pase", "Defensa"]
        self._quimica = 100
    
    #nro1=89
    #nro2=99
    
    def setAtributos(self):
        super().setAtributos()
        numero = round(randint(89,99) * 1.02)
        if  numero > 99:
            return 99
        else:
            return numero

        self._velocidad += round(self._velocidad * 0.02)
        if self._velocidad > 99:
            self._velocidad = 99
        self._tiro += round(self._tiro * 0.02)
        if self._tiro > 99:
            self._tiro = 99
        self._regate += round(self._regate * 0.02)
        if self._regate > 99:
            self._regate = 99
        self._defensa += round(self._defensa * 0.02)
        if self._defensa > 99:
            self._defensa = 99
        self._pase += round(self._pase * 0.02)
        if self._pase > 99:
            self._pase = 99
        self._fisico += round(self._fisico * 0.02)
        if self._fisico > 99:
            self._fisico = 99
    def quimicaza(self, paisFav, equipoFav):
        super().quimicaza(paisFav, equipoFav)
        
    def imprimirCarta(self):
        super().imprimirCarta()
        print("Habilidad especial:", *self._habilidadEspecial)