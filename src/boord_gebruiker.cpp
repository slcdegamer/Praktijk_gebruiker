#include <Arduino.h>
#include <iostream>
#include <string>
int drempel = 0;
String output = "";

std::string text = "0000";
String  tekst = text.c_str();
char lezen = '0';
int sensorValue= 1000;
char gelezen = '0';       

void setup() {
  pinMode(4, OUTPUT);
  pinMode(A0,INPUT);
  Serial.begin(9600);
  drempel= analogRead(A0)+20;
 
}
void loop() {
  
  Serial.println();
  int sensorValue = analogRead(A0);
  
  if(lezen == '0'){text.erase(0, 1);}
  if (sensorValue>drempel ){ Serial.println("1");text.push_back('1');  gelezen = '1';}
  else{Serial.println("0");text.push_back('0'); gelezen = '0';}
  
  Serial.println(sensorValue);
  
  String tekst = text.c_str();
  Serial.println(tekst);
  if(tekst=="1001"){lezen = '1';Serial.println("tekst"); }
  int start = tekst.length() - 4;
  String laatste4 = tekst.substring(start, tekst.length());
  delay(500);
  if(laatste4 == "1111" and lezen == '1'){Serial.println(tekst);text = "0000";lezen = '0';}
  
  while(Serial.available()>0){
    output = Serial.readStringUntil('\n');
    for (int i = 0; i<output.length(); i+=1){
      char bit = output[i];
      if(bit == '1'){digitalWrite(4, HIGH);}
      else { digitalWrite(4, LOW);}
      delay(500);
    }
  }
  digitalWrite(4, LOW);
}
