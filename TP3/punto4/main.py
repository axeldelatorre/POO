from random import*
from guerrero import Guerrero
from mago import Mago
guerrero1 = Guerrero(None, 70, 50)
maguinho = Mago(None, 40, 80)
i = 0
while maguinho.vivo() and guerrero1.vivo():
    i += 1
    print("                               <<<<<<<<<<<<<<<< RONDA",i," >>>>>>>>>>>>>>>>>>>")
    if randint(0,1) ==1:
        maguinho.defender(guerrero1.atacar())
    else:
        guerrero1.defender(maguinho.atacar())
if maguinho.vivo():
    print("                        <<<<<<<<<<<< El", maguinho._nombre, "gano la partida!!! >>>>>>>>>>>")
else:
    print("                        <<<<<<<<<<<< El", guerrero1._nombre, "gano la partida!!! >>>>>>>>>>>")