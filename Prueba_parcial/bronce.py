from random import*
from carta import Carta

class BronceEspecial(Carta):
    def __init__(self,nombre, club, pais, habilidadEspecial, quimica):
        super().__init__(nombre, club, pais, habilidadEspecial, quimica)
    
    def setAtributos(self):
        super().setAtributos()
        return round(randint(49, 65) + 2)
        
    def quimicaza(self, paisf, equipof):
        super().quimicaza(paisf, equipof)
        
    
    def imprimirCarta(self):
        super().imprimirCarta()
        print("Habilidad Especial:",self._habilidadEspecial)
        
    