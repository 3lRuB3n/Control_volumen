import even, recep as rec, ControlDisplay as CD, esp
from time import sleep as sl
error = 0
disp = 0
ind = 0

#aqui van los receptores con la direccion fisica y la mac
disp = rec.recep("test", "0",0, 'u'), rec.recep("USB","0",1,'u'), rec.recep("ESPNow","AABBCCDDEEFF",0,'a')
Ndisp = len(disp)

esp.setup(disp)

while error == 0:
    sl(0.01)
    pend, comandos = even.actu(even.pines)
    rotacion = even.act_inc(even.encoder)
    CD.apaga()
    if pend:
        for i in comandos:
            CD.ilumina(i)
            if i == "disp":
                ind = (ind+1)%Ndisp
                CD.g_rec[0] = disp[ind].img #cambia la imagen del receptor a la del dispositivo de turno
            else:
                disp[ind].envia(i)
    if rotacion != 0:
        CD.ilumina("altavoz")
        rec.envia_audio(rotacion, disp[ind])
        CD.g_altavoz[0] = 0 if rotacion>0 else 1
        CD.g_altavoz.hidden = False