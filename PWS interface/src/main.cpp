#include <Arduino.h>

int ledPin = 4;   // variabele die we willen lezen
int drempel = 800;
bool doorgaan = true;
String input = "";
int waarde = 0;
char c= ' ';
String output = "";

void setup() {
  Serial.begin(9600);   
  pinMode(ledPin, OUTPUT);
  pinMode(A0,INPUT);
  digitalWrite(ledPin, HIGH);
}

void loop() {
  
  doorgaan = true;
  if (analogRead(A0)>drempel){
    String byte = "";
    for (int i = 0; i<4; i+=1){
      if(analogRead(A0)>drempel){byte = byte + '1'; Serial.println('1');}
      else{byte = byte + '0';Serial.println('0');}
      delay(1000);
      Serial.println(byte);
    
    if (byte == "1001"){
    
      input = "1001";
      
      while(doorgaan){
        waarde = analogRead(A0);
        
        if(waarde>drempel){
          c = '1';
        } else { c = '0';}
        input += c;
        
        int start = input.length() - 3;
        String laatste3 = input.substring(start, input.length());
        delay(1000);
        if(laatste3 == "111"){
          doorgaan = false;
          Serial.println(input);
            
          }
          

        }
      } 
    }
  }

  delay(1000);
  
  // leest de verstuurde string van bits vanaf python en laat het lampje knipperen
  while(Serial.available()>0){
    output = Serial.readStringUntil('\n');
    for (int i = 0; i<output.length(); i+=1){
      char bit = output[i];
      if(bit == '1'){digitalWrite(ledPin, HIGH);}
      else { digitalWrite(ledPin, LOW);}
      delay(50);
    }
    digitalWrite(ledPin, LOW);

  }
}
