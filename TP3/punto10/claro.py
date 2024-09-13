from tarifaProveedor import TarifaProveedor
class Claro(TarifaProveedor):
    def __init__(self, totalSms, totalMinutos, totalGigas):
        super().__init__(totalSms, totalMinutos, totalGigas)
        self._sms *= 1.20
    
    def calcularSMS(self):
        return super().calcularSMS()
    
    def calcularMinutos(self):
        return super().calcularMinutos()
    
    def calcularGigas(self):
        return super().calcularGigas()
    
    def getNombre(self):
        return print(type(x).__name__)
        
    
x = Claro(None, None, None)