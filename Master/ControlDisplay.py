import displayio as dio
import adafruit_displayio_sh1106, board, busio, os
import Cadena2Imagen as im
from time import monotonic as t_act

dio.release_displays()

#El ancho tiene que ser 130, si no habrá leak de memoria en la pantalla
ancho, alto = 130, 64												##SCL, SDA
display = adafruit_displayio_sh1106.SH1106(dio.I2CDisplay(busio.I2C(board.GP19, board.GP18), device_address=0x3C), width=ancho, height=alto)

#Paleta
paleta = dio.Palette(2)
paleta[0] = 0
paleta[1] = 0xFFFFFF

#Crea el grupo base
marco = dio.Group()
display.root_group = marco
marco.x = 2
marco.y = 0

os.chdir("/imagenes")

#Convierte las imagenes almacenadas en txt a un bitmap de displayio
receptores = im.btm("receptores.txt")
onOff = im.btm("onOff.txt")
playPau = im.btm("playPau.txt")
prev = im.btm("prev.txt")
sig = im.btm("sig.txt")
altavoz = im.btm("altavoz.txt")
camb = im.btm("camb.txt")

#Crea los grupos con sus respectivos sprites / spritesheets
g_rec = dio.TileGrid(receptores.mapa, pixel_shader=paleta, width=1, height=1, tile_width=32, tile_height=46)
g_onOff = dio.TileGrid(onOff.mapa, pixel_shader=paleta)
g_playPau = dio.TileGrid(playPau.mapa, pixel_shader=paleta)
g_prev = dio.TileGrid(prev.mapa, pixel_shader=paleta)
g_sig = dio.TileGrid(sig.mapa, pixel_shader=paleta)
g_disp = dio.TileGrid(camb.mapa, pixel_shader=paleta)
g_altavoz = dio.TileGrid(altavoz.mapa, pixel_shader=paleta, width=1, height=1, tile_width=19, tile_height=17)

#Añade los grupos al marco principal
marco.append(g_rec)
marco.append(g_onOff)
marco.append(g_playPau)
marco.append(g_prev)
marco.append(g_sig)
marco.append(g_altavoz)
marco.append(g_disp)
    
#Extraidos del .aseprite, añadiendo 2 a la coordenada y de cada grupo por problemas de dimensionamiento del display
g_rec.x, g_rec.y = 1, 9
g_onOff.x, g_onOff.y = 98, 11
g_playPau.x, g_playPau.y = 72, 40
g_prev.x, g_prev.y = 49, 40
g_sig.x, g_sig.y, = 98, 40
g_altavoz.x, g_altavoz.y, = 73, 12
g_disp.x, g_disp.y, = 49, 12

t_encen = 0
def apaga():	#Que se apague x tiempo usando una variable global y monotonic
    global t_encen
    if t_act() > t_encen + 1:
        g_onOff.hidden = True
        g_playPau.hidden = True
        g_prev.hidden = True
        g_sig.hidden = True
        g_altavoz.hidden = True
        g_disp.hidden = True
    
def ilumina(mensaje): #Activa el grupo de turno
    global t_encen
    t_encen = t_act()
    #print(mensaje)
    dicc = {"ant":g_prev,
            "sig":g_sig,
            "playPau":g_playPau,
            "disp":g_disp,
            "altavoz":g_altavoz,
            "onOff": g_onOff,
            "sil": g_altavoz
            }
    dicc.get(mensaje).hidden = False