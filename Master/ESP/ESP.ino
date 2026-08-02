/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp-now-esp8266-nodemcu-arduino-ide/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/
//habría que cambiar los println por print, o recortar los mensajes que mande en el receptor (La raspberrry pi pico, con circuitpython)

#include <ESP8266WiFi.h>
#include <espnow.h>

byte dir[] = {0,0,0,0,0,0}; //max 20 por limitaciones de ESPNow
esp_now_peer_info_t peerInfo;

byte onDataSent(byte *mac_addr byte sendStatus){
  return sendStatus
}

void setup(){
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) return; 
  Serial.println("ok");

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);

  esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop(){
  while(!Serial.available()){}
  String data = Serial.readString();  //mensaje compuesto por la dir mac del receptor en hexadecimal con mayusculas y el comando, sin espacios
  data.trim();
  String dir_char = data.substring(0,12);
  Serial.println(dir_char);
  for(int i=0;i<11;i+=2){
    dir[i/2] = char2hex(dir_char[i])*16 + char2hex(dir_char[i+1]);
  }
  String mensaje = data.substring(12);
  
}

byte char2hex(char letra){
  if(letra >= '0' && letra <= '9') 
    return letra - '0';
  else if(letra >= 'A' && letra <= 'F')
    return letra - 'A' + 10;
  else return 0;
}