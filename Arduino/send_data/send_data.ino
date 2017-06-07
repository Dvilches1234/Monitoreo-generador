a#include <Ethernet.h>


byte mac[] = { 0x00, 0xAB, 0xBC, 0xCC, 0xDE, 0x01 }; 
EthernetClient client;

//variables intensity
float input_voltage = 0.0;
float intensity = 0;
float res = 1340 ;
//
//variables wind speed
float begin_time = 0;
float medition_time = 0;
float wind_speed = 0;
int inpin = 2;
//



void setup(){
  Serial.begin(9600);
  pinMode(inpin, INPUT);y
  if (Ethernet.begin(mac) == 0){
    Serial.println("Failed to configure Ethernet using DHCP");
  }
  delay (3000);
}

void loop(){

 
   int analog_value = analogRead(A1);
   input_voltage = (analog_value * 5.0) / 1024.0; 

   
   if (input_voltage < 0.02) 
   {
     input_voltage=0.0;
   }
  intensity = input_voltage * 100000/ res;
  
  attachInterrupt(digitalPinToInterrupt(inpin), calculate_speed, RISING);
   
  if(client.connect("http://localhost:5000" , 5000)){
   client.println("POST /data", data={'i':intensity, 'v' = windspeed} 
  }
 
  
}

void calculate_speed(){
  medition_time = millis();
  if(begin_time == 0){
    begin_time = medition_time;
    break;
  }
  float delta = medition_time - begin_time;
  float angular = 3.14159 / delta;
  wind_speed = angular * 0.07;
  begin_time = medition_time;
}

