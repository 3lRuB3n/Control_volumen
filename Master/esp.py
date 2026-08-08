import board, busio, digitalio as dio
from time import sleep as sl

led = dio.DigitalInOut(board.LED)
led.switch_to_output()
                    #Rx, Tx
uart = busio.UART(board.GP17, board.GP16, baudrate = 74880) #ya se verán los pines

def limpia(lec):
    men = ''
    print(lec)
    if lec != None:
        men = ''.join([chr(b) for b in lec])
        return men


print("esperando ESP")
led.value = True
lectura = ''
while lectura != "ok":
    lectura = limpia(uart.read(2))
    sl(0.05)
print("esp listo")
led.value = False
estado = 0

def nada():
    global estado
    uart.write('a')
    estado = -1
    led.value = False

def setup(dispositivos):
    led.value = True
    Nmacs = 0
    Macs = []
    for i in dispositivos:
        if i.macs != "0":
            Macs.append(i.mac)
    uart.write('a'+len(Macs)) #del 0 al 20
    for m in Macs:
        uart.write(m) #va a dar problemas, deben ser bytes en vez de strings...
        sl(.01)
        
    while uart.read != "okk":
        pass
    led.value = False
    
def envia_espnow(comm):
    mens = self.letra
    mens.append(comm)
    uart.write(mens)