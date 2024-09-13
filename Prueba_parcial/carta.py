from random import*
class Carta:
    def __init__(self, nombre, club, pais, habilidadEspecial, quimica):
        self._nombre = nombre
        self._club = club
        self._pais = pais
        self._habilidadEspecial = habilidadEspecial
        self._velocidad = self.setAtributos()
        self._tiro = self.setAtributos()
        self._regate = self.setAtributos()
        self._defensa = self.setAtributos()
        self._pase = self.setAtributos()
        self._fisico = self.setAtributos()
        self._quimica = quimica
        
    def setAtributos(self):
        pass
    
    def quimicaza(self, paisf, equipof):
        if self._pais == paisf and self._club == equipof:
            self._quimica = 100
        elif self._pais == paisf or self._club == equipof:
            self._quimica = 80
        else:
            self._quimica = 0
        return self._quimica
    
    def imprimirCarta(self):
        print("_____________________________________________")
        print("<<<<<<",self._nombre, ">>>>>>")
        print("Club:",self._club)
        print("Pais:",self._pais)
        print("Velocidad:",self._velocidad)
        print("Tiro:",self._tiro)
        print("Regate:",self._regate)
        print("Defensa:",self._defensa)
        print("Pase:",self._pase)
        print("Fisico:",self._fisico)
        print("Quimica:",self._quimica)