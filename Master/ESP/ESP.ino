#include <ESP8266WiFi.h>
#include <espnow.h>

#define println Serial.println      //habría que cambiar los println por print, o recortar los mensajes que mande en el receptor (La raspberrry pi pico, con circuitpython)

unsigned char dir[20*6]; //20 direcciones máximas (cosas de esp_now) y 6 bytes (ordenados así por cosas de las ip)

void setup(){
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  println("on");
  if (esp_now_init() != 0) return; 
  println("ok");

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(onDataSent);

  addPeers();
}

void loop(){
  String data = leer();
  unsigned char obj = letraA20(data[0]);
  String mensaje = data.substring(1);
  
  esp_now_send(dir+obj*6, (uint8_t *) &mensaje, sizeof(mensaje)); //mete esto en un do while, puede que lo de la dirección no le haga gracia a la funcion esta
}

void addPeers(){
   int N_rec = letraA20(leer()[0]); //a=0, b=1, c=2 ... u=20
   if(N_rec == 0){
    ESP.deepSleep(0); //Se pone en stand-by hasta que se reinicie
   }
   for(int j = 0;j<N_rec;j++){
    String dir_char = leer(); //lee la siguiente dirección
    for(int i=0;i<11;i+=2){
      dir[j*6+i/2] = char2hex(dir_char[i])*16 + char2hex(dir_char[i+1]);
    }
   }
  println("anhadidos");
}

String leer(){ //leer el puerto serie comprimido a una sola funcion. Puede que sobre el delay o que sea excesivo (seguramente)
  //println("escuchando");
  while(!Serial.available()){
    delay(100);
  }
  String dato = Serial.readString();
  dato.trim();
  //println(dato);
  return dato;
}

byte char2hex(char letra){
  if(letra >= '0' && letra <= '9') 
    return letra - '0';
  else if(letra >= 'A' && letra <= 'F')
    return letra - 'A' + 10;
  else return 0;
}

byte letraA20(char letra){
  //println(letra - 'a');
  return letra - 'a';
}

void onDataSent(byte *mac_addr, byte sendStatus){
  println(sendStatus);
}