import esp, even, recep as rec, ControlDisplay as CD
from time import sleep as sl
from time import monotonic as t_act
error = 0
disp = 0
ind = 0

t_espera = 30 #seg
t_even = t_act()
on = True

#aqui van los receptores con la direccion fisica y la mac
disp = rec.recep("test", "0",0, 'u'), rec.recep("USB","0",1,'u')#, rec.recep("ESPNow","40915151EDA2",3,'a')
Ndisp = len(disp)
CD.g_rec[0] = disp[ind].img
#esp.setup(disp)

while True:
    if t_act() > t_even + t_espera:
        on = False
        
    CD.marco.hidden = not on
    sl(0.01)
    pend, comandos = even.actu(even.pines)
    rotacion = even.act_inc(even.encoder)
    CD.apaga()
    if pend and on: #Todo lo que tenga que ver con botones
        t_event = t_act()
        for i in comandos:
            if i == "sil":
                CD.g_altavoz[0] = 2
            CD.ilumina(i)
            if i == "disp":
                ind = (ind+1)%Ndisp
                CD.g_rec[0] = disp[ind].img #cambia la imagen del receptor a la del dispositivo de turno
            else:
                disp[ind].envia(i)
    if rotacion != 0 and on:
        t_event = t_act()
        CD.g_altavoz[0] = 0 if rotacion>0 else 1
        CD.ilumina("altavoz")
        rec.envia_audio(rotacion, disp[ind])
        CD.g_altavoz.hidden = False
        
    if (rotacion != 0 or pend) and not on:
        on = True
        t_even = t_act()