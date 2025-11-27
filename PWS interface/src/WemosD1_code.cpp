#include <Arduino.h>
#include <string>

int LED_PIN = 4; // sluit de kabel van de het LEDlampje aan op pin D2. pin D2 = pin 4 
int LDR_PIN = A0; // sluit de kabel van de LDR aan op pin A0

String output = "";
std::string text = "00000000";
String  tekst = text.c_str();
int drempel = 0;
char lezen = '0';
char gelezen = '0';    
bool print_bits = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(LDR_PIN,INPUT); 
  Serial.begin(9600);
  drempel= analogRead(LDR_PIN)+100; 
}

void loop() {
  
  int sensorValue = analogRead(LDR_PIN);
  
  if(lezen == '0'){text.erase(0, 1);} // laatste bit wordt verwijderd en gelezen bit wordt toegevoegd
  if (sensorValue>drempel ){text.push_back('1');  gelezen = '1';}
  else{text.push_back('0'); gelezen = '0';}
  
  String tekst = text.c_str();
  
  if(print_bits == true){Serial.println(tekst);}
  if(tekst=="10000001"){lezen = '1';Serial.println("tekst");}
  
  int start = tekst.length() - 8;
  String laatste8 = tekst.substring(start, tekst.length());
  if(laatste8 == "11111111" and lezen == '1'){Serial.println("Bericht");Serial.println(tekst);text = "00000000";lezen = '0';}

  delay(100);
  
  while(Serial.available()>0){ // als de interface een pakketje stuurt dan detecteert de functie dat er iets in de wachtrij staat en verzend het het pakketje 
    output = Serial.readStringUntil('\n');
    if(output == "a"){delay(25);Serial.println("DELAY");}
    if(output == "b"){print_bits = !print_bits;Serial.println("print bits omgekeerd");}
    for (int i = 0; i<output.length(); i+=1){
      char bit = output[i];
      if(bit == '1'){digitalWrite(LED_PIN, HIGH);}
      else { digitalWrite(LED_PIN, LOW);}
      delay(100);
    }
  }
  digitalWrite(LED_PIN, LOW);
}