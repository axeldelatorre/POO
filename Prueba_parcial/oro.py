from random import*
from carta import Carta
class Oro(Carta):
    def __init__(self,nombre, club, pais, habilidadEspecial, quimica):
        super().__init__(nombre, club, pais, habilidadEspecial, quimica)
    
    #nro1=74
    #nro2=90
    
    def setAtributos(self):
        super().setAtributos()
        return round(randint(74, 90) * 1.05)
        
    def quimicaza(self, paisf, equipof):
        super().quimicaza(paisf, equipof)
    
    def imprimirCarta(self):
        super().imprimirCarta()