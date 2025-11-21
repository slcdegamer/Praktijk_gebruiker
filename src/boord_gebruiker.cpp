#include <Arduino.h>
#include <iostream>
#include <string>
int drempel = 0;
String output = "";

std::string text = "00000000";
String  tekst = text.c_str();
char lezen = '0';
int sensorValue= 1000;
char gelezen = '0';    
bool begon = false; 
int i = 0;

void setup() {
  pinMode(4, OUTPUT);
  pinMode(A0,INPUT);
  Serial.begin(9600);
  drempel= analogRead(A0)+30;
  delay(5000);
  Serial.println(drempel);
  delay(5000);
 
}
void loop() {
  
  //Serial.println();
  int sensorValue = analogRead(A0);
  
  // laatste bit wordt verwijderd en de nieuwe gelezen bit wordt toegevoegd 
  if(lezen == '0'){text.erase(0, 1);}
  if (sensorValue>drempel ){text.push_back('1');  gelezen = '1';}
  else{text.push_back('0'); gelezen = '0';}
  
  //Serial.println(sensorValue);
  
  String tekst = text.c_str();
  Serial.println(tekst);
  if(tekst=="10000001"){lezen = '1';Serial.println("tekst"); begon = true;}
  
  //int delayd = 100;
  //int start2 = tekst.length() - 2;
  //String laatste2 = tekst.substring(start2, tekst.length());

  //if(laatste2 == "11" && begon == false){delayd=150;Serial.println("vertraagd");}
  
  int start = tekst.length() - 8;
  String laatste4 = tekst.substring(start, tekst.length());
  delay(1000);
  Serial.println(i);
  i=i+1;

  
  if(laatste4 == "11111111" and lezen == '1'){Serial.println("Bericht");Serial.println(tekst);text = "00000000";lezen = '0';begon = true;}
  
  while(Serial.available()>0){
    output = Serial.readStringUntil('\n');
    //Serial.println(output);
    //Serial.println("TEKST");
    if(output == "a"){delay(500);Serial.println("DELAY");}
    for (int i = 0; i<output.length(); i+=1){
      char bit = output[i];
      if(bit == '1'){digitalWrite(4, HIGH);}
      else { digitalWrite(4, LOW);}
      delay(100);
    }
  }
  digitalWrite(4, LOW);
}
