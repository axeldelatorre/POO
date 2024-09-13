from tarifaProveedor import TarifaProveedor
from claro import Claro
from personal import Personal
from movistar import Movistar

tarifa1 = Claro(20, 3000, 10)
tarifa2 = Personal(20, 3000, 10)
tarifa3 = Movistar(20, 3000, 10)

tarifa1.getNombre()
tarifa1.imprimir()
print("")
tarifa2.getNombre()
tarifa2.imprimir()
print("")
tarifa3.getNombre()
tarifa3.imprimir()