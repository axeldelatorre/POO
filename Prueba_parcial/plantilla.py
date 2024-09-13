
class Plantilla():
    def __init__(self, usuario, paisFav, equipoFav):
        self._usuario = usuario
        self._paisFav = paisFav
        self._equipofav = equipoFav
        self._plantel = []
    
    def agregar(self, cartaza):
        self._plantel.append(cartaza)
    
    def quimicatotal(self):
        total= 0
        for x in self._plantel:
            total += x._quimica
        total = total/len(self._plantel)
        return total
        
    def impimirPlantilla(self):
        print("Usuario:", "<<<<<<<<<", self._usuario, ">>>>>>>>>>")
        print("Pais:","<<<<<<<<<", self._paisFav, ">>>>>>>>>>")
        print("Equipo:","<<<<<<<<<", self._equipofav, ">>>>>>>>>>")
    
    def imprimirPlantel(self):
        for x in self._plantel:
            x.imprimirCarta
        