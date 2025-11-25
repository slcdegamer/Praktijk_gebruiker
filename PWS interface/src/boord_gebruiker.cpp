#include <Arduino.h>
#include <iostream>
#include <string>

int drempel = 0;
String output = "";
std::string text = "00000000";
String  tekst = text.c_str();
char lezen = '0';
char gelezen = '0';    
bool print_bits = false;

void setup() {
  pinMode(4, OUTPUT); // kabel LED lamp aansluiten op pin D2
  pinMode(A0,INPUT); // kabel van de LDR aansluiten op pin A0
  Serial.begin(9600);
  drempel= analogRead(A0)+100;
  delay(5000);
  Serial.println(drempel);
  delay(5000);
}

void loop() {
  
  int sensorValue = analogRead(A0);
  
  if(lezen == '0'){text.erase(0, 1);} // laatste bit wordt verwijderd en gelezen bit wordt toegevoegd
  if (sensorValue>drempel ){text.push_back('1');  gelezen = '1';}
  else{text.push_back('0'); gelezen = '0';}
  
  String tekst = text.c_str();
  
  if(print_bits == true){Serial.println(tekst);}
  if(tekst=="10000001"){lezen = '1';Serial.println("tekst");}
  
  int start = tekst.length() - 8;
  String laatste8 = tekst.substring(start, tekst.length());
  if(laatste8 == "11111111" and lezen == '1'){Serial.println("Bericht");Serial.println(tekst);text = "00000000";lezen = '0';}

  delay(200);
  
  while(Serial.available()>0){ // als de interface een pakketje stuurt dan detecteert de functie dat er iets in de wachtrij staat en verzend het het pakketje 
    output = Serial.readStringUntil('\n');
    if(output == "a"){delay(25);Serial.println("DELAY");}
    if(output == "b"){print_bits = !print_bits;Serial.println("print bits omgekeerd");}
    for (int i = 0; i<output.length(); i+=1){
      char bit = output[i];
      if(bit == '1'){digitalWrite(4, HIGH);}
      else { digitalWrite(4, LOW);}
      delay(200);
    }
  }
  digitalWrite(4, LOW);
}
