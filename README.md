# Instalación
## Requisitos
Circuitpython 
# Componentes y conexiones
A la hora de fabricar el hardware de este proyecto se han usado como base para las conexiones dos placas perforadas de 5x7cm.
## Componentes
- 1 Raspberry pi pico (Puede que funcione con una Raspberry pi pico 2)
- Módulo ESP01/ESP01s
- Pantalla oled 1.3in con controlado SH1106
- 5 Pulsadores del tipo (?) de 6x6x11.5 mm
- 1 Codificador rotativo del tipo EC11
- 1 Resistencia Pull-Up para el ESP01
## Conexiones
1. GP20, GP21: A, B codificador
2. GP6: Pulsador **Silenciar**
3. GP13: Pulsador **Siguiente** pista
4. GP15: Pulsador pista **Anterior**
5. GP14: Pulsador **Play/Pausa**
6. GP5: Pulsador **Cambio Dispositivo**
7. GP28: Pulsador **On/Off**

# Estructuras de los programas
## Estructura del programa de la Raspberry Pi
1. Code.py; Donde ocurre el bucle principal.
2. ControlDisplay.py; Encargado del control del SH1106.
3. Cadena2Imagen.py; Convierte un txt a bitmap de displayio
4. even.py; Encargado de declarar los inputs del dispositivo
5. recep.py; Alberga la clase **recep** y los métodos de envío a los dispositivos conectados por USB
6. wled.py; #TODO, capa de traducción de las funciones de esp.py para que las reconozca un dispositivo WLED
7. esp.py; Encargado de la comunicación con el módulo ESP01/01s, encargado de enviar comandos mediante ESPNow a otros receptores.
## Estructura del programa del ESP maestro
#TODO
## Estructura del programa del ESP esclavo
#TODO 
