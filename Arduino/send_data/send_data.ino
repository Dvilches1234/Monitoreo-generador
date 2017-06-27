/*#include <Ethernet.h>

int medition_time = 2000;
byte mac[] = { 0x00, 0xAB, 0xBC, 0xCC, 0xDE, 0x01 }; 
EthernetClient client;
*/

//variables time
int medition_time = 2000;
int next_medition;
//variables intensity
float input_voltage = 0.0;
float intensity = 0;
float res = 1340 ;
//
//variables wind speed
int revs = 0;
bool last_state = false;
float pi = 3.14159;
float r = 0.07;
int inpin = 2;
float wind_speed;
//


void setup(){
  Serial.begin(9600);
  pinMode(inpin, INPUT);
  digitalWrite(inpin, LOW);
  next_medition = millis() + medition_time;
}

void loop(){
  int time = millis(); 
  if (digitalRead(inpin) == HIGH){
   if (last_state == false)
     revs++;
   last_state = true; 
   }else{
    last_state = false;
   }
   if (time >= next_medition){
     int analog_value = analogRead(A1);
     input_voltage = (analog_value * 5.0) / 1024.0; 
   
     if (input_voltage < 0.02) 
     {
       input_voltage=0.0;
     }
     
     intensity = input_voltage * 100000/ res;
     calculate_speed();
 
     Serial.print("i ");
     Serial.println(intensity,4);
     Serial.print("v ");
     Serial.println(wind_speed);
     next_medition += medition_time;
   }else{
     Serial.print("i ");
     Serial.println(-1);
     Serial.print("v ");
     Serial.println(-1);
   }
  
}

void calculate_speed(){
   int delta = medition_time /1000;
   float angular = revs * pi /delta;
   wind_speed = angular * r * 3.6;
   revs = 0;
}

