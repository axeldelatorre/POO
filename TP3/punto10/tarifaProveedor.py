class TarifaProveedor:
    def __init__(self, totalSMS, totalMinutos, totalGigas):
        self._sms = 1
        self._minutos = 15
        self._gigas = 20
        self._totalSMS = totalSMS
        self._totalMinutos = totalMinutos
        self._totalGigas = totalGigas
    def calcularSMS(self):
        self._totalSMS *= self._sms
        return self._totalSMS
    def calcularMinutos(self):
        self._totalMinutos *= self._minutos
        return self._totalMinutos
    def calcularGigas(self):
        self._totalGigas *= self._gigas
        return self._totalGigas
    def calcular(self):
        return (self._totalSMS + self._totalMinutos + self._totalGigas)
    def getNombre(self):
        pass
    
    def imprimir(self):
        print("Importe total SMS:", self.calcularSMS())
        print("Importe total Llamadas:", self.calcularMinutos())
        print("Importe total Gigas:", self.calcularGigas())
        print("")
        print("Importe total a pagar:", self.calcular())