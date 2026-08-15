import board, digitalio as dio
from rotaryio import IncrementalEncoder as IE
                #?? lo mismo es al reves
encoder = [IE(board.GP20, board.GP21), 0] #encoder + posicion antigua

class flanco:
    def __init__(self, pin, mensaje):
        self.pin = pin
        self.ant = pin.value
        self.val = False
        self.mens = mensaje
    def check(self):
        res = not self.val and self.pin.value
        self.val = self.pin.value
        return res
pines = []

sil = flanco(dio.DigitalInOut(board.GP26),"sil")
sil.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(sil)

sig = flanco(dio.DigitalInOut(board.GP13),"sig") #13
sig.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(sig)

ant = flanco(dio.DigitalInOut(board.GP15),"ant") #15
ant.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(ant)

playPau = flanco(dio.DigitalInOut(board.GP14),"playPau")
playPau.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(playPau)

disp = flanco(dio.DigitalInOut(board.GP3),"disp") #(?)
disp.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(disp)

onoff = flanco(dio.DigitalInOut(board.GP27),"onOff") #15?
onoff.pin.switch_to_input(pull=dio.Pull.DOWN)
pines.append(onoff)


def actu(pines):
    pendiente = False
    pend = []
    for i in pines:
        if i.check():
            pendiente = True
            pend.append(i.mens)
    return(pendiente, pend)

def act_inc(encoder):
    diff = encoder[0].position - encoder[1]
    encoder[1] = encoder[0].position
    return diff