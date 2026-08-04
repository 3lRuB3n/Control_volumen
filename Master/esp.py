import board, busio, digitalio as dio
from time import sleep as sl

led = dio.DigitalInOut(board.GP1)
led.switch_to_output()

uart = busio.UART(board.TX, board.RX, baudrate = 115200) #ya se verán los pines

print("esperando ESP")
led.value = True
while uart.read(2) != "ok":
    pass
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
        if i.macs != "0"
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