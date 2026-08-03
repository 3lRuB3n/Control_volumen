from usb_hid import devices as dev
from adafruit_hid.consumer_control_code import ConsumerControlCode as CCC
from adafruit_hid.consumer_control import ConsumerControl as CC
cc = CC(dev)

def envia_hid(st):
    dicc = {"sil":CCC.MUTE,
            "playPau":CCC.PLAY_PAUSE,
            "sig":CCC.SCAN_NEXT_TRACK,
            "ant":CCC.SCAN_PREVIOUS_TRACK,
            "volMen":CCC.VOLUME_DECREMENT,
            "volMas":CCC.VOLUME_INCREMENT,
            "onOff":113 #Creo que fn+f5
            }
    cc.send(dicc.get(st))

def envia_audio(dif, recep):
    codigo = "volMas" if dif > 0 else "volMen"
    for i in range(abs(dif)):
        recep.envia(codigo)

class recep:
    def __init__(self, Dir, MAC):
        self.dir = Dir
        if Dir == "USB":
            self.envia = envia_hid
        elif Dir == "test":
            self.envia = print
        elif Dir == "wled":
            self.envia = envia_wled
            self.mac = MAC
        elif Dir == "ESPNow":
            self.envia = esp.envia_espnow
            self.mac = MAC