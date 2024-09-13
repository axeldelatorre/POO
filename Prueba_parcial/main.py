#from carta import Carta
from random import*
from bronce import BronceEspecial
from oro import Oro
from especial import Especial
from plantilla import Plantilla

Jugadores = ["Riquelme","Zidane", "Pinino Mas", "Zico","Ronaldo","Battaglia", "Equi Fernandez", "Juan sebastian Veron","Francesco Totti", "Pomelo Vera","Martin Rolle"]
Habilidades_especiales = ["Ataque", "Pase", "Defensa"]
Clubes= ["Arsenal", "Montevideo City Torque", "Inter Miami", "Manchester City"]
Paises= ["Argentina", "Inglaterra", "Holanda", "Japon"]

Cartas = []

plantilla1 = Plantilla("Axel", choice(Paises), choice(Clubes))
plantilla2 = Plantilla("Martin", choice(Paises), choice(Clubes))
print("")
for n in range(22):
    carta1 = BronceEspecial(choice(Jugadores), choice(Clubes), choice(Paises),choice(Habilidades_especiales), None)
    carta2 = Oro(choice(Jugadores),choice(Clubes), choice(Paises), None, None)
    carta3 = Especial(choice(Jugadores),choice(Clubes), choice(Paises), None, None)
    carta2.quimicaza(plantilla1._paisFav, plantilla1._equipofav)
    carta1.quimicaza(plantilla1._paisFav, plantilla1._equipofav)
    Cartas.append(carta1)
    Cartas.append(carta2)
    Cartas.append(carta3)
shuffle(Cartas)
i=0
for x in Cartas:
    if i <11:
        plantilla1.agregar(x)
        i+=1
i=0
for x in Cartas:
    if i <11:
        plantilla2.agregar(x)
        i+=1
        
plantilla1.impimirPlantilla()
print("Quimica:",round(plantilla1.quimicatotal()), "GRL")

for x in plantilla1._plantel:
    x.imprimirCarta()
    
print("")

plantilla2.impimirPlantilla()
print("Quimica:",round(plantilla1.quimicatotal()), "GRL")

for x in plantilla2._plantel:
    x.imprimirCarta()