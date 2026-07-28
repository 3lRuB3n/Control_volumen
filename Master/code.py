import even, recep as rec, ControlDisplay as CD
from time import sleep as sl
error = 0
disp = 0
ind = 0

disp = rec.recep("test"), rec.recep("USB")
Ndisp = len(disp)

while error == 0:
    sl(0.01)
    pend, comandos = even.actu(even.pines)
    rotacion = even.act_inc(even.encoder)
    CD.apaga()		#Hay que rehacerla
    if pend:
        for i in comandos:
            CD.ilumina(i)
            if i == "disp":
                ind = (ind+1)%Ndisp
                CD.g_rec[0] = ind
            else:
                disp[ind].envia(i)
    if rotacion != 0:
        CD.ilumina("altavoz")
        rec.envia_audio(rotacion, disp[ind])
        CD.g_altavoz[0] = 0 if rotacion>0 else 1
        CD.g_altavoz.hidden = False
        