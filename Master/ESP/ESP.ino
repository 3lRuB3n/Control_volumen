#include <ESP8266WiFi.h>
#include <espnow.h>

#define println Serial.println      //habría que cambiar los println por print, o recortar los mensajes que mande en el receptor (La raspberrry pi pico, con circuitpython)

byte dir[20][6]; //20 direcciones máximas (cosas de esp_now) y 6 bytes (ordenados así por cosas de las ip)
//esp_now_peer_info_t peerInfo;

void setup(){
  Serial.begin(115200);
  //WiFi.mode(WIFI_STA);

  /*if (esp_now_init() != ESP_OK) return; 
  Serial.println("ok");

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);*/

  addPeers();
}

void loop(){
  String data = leer();
  int obj = letraA20(data[1]);
  String mensaje = data.substring(2);
  //abajo toca hacer cositas con los punteros, de momento no se que le pasa a esto, mejor miralo en un compilador online de c y luego intenta implementarlo
  esp_now_send(dir + (sizeof)*(obj), mensaje, sizeof(mensaje)); //mete esto en un do while, puede que lo de la dirección no le haga gracia a la funcion esta
}

void addPeers(){
   int N_rec = letraA20(leer()[0]); //a=0, b=1, c=2 ... u=20
   if(N_rec == 0){
    println("Apagando");
    //ESP.deepSleep(0); //Se pone en stand-by hasta que se reinicie
   }
   for(int j = 0;j<N_rec;j++){
    for(int i=0;i<11;i+=2){
      String dir_char = leer(); //lee la siguiente dirección
      dir[j][i/2] = char2hex(dir_char[i])*16 + char2hex(dir_char[i+1]);
    }
   }
  println("anhadidos");
}

String leer(){ //leer el puerto serie comprimido a una sola funcion. Puede que sobre el delay o que sea excesivo (seguramente)
  while(!Serial.available()){
    delay(100);
  }
  String dato = Serial.readString();
  dato.trim();
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
  return letra - 'a';
}

/*byte onDataSent(byte *mac_addr byte, sendStatus){
  println(sendStatus);
} */