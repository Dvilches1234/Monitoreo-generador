
float begin_time = 0;
float medition_time = 0;
float wind_speed = 0;
int inpin = 2;
int in = 0;
void setup() {
  Serial.begin(9600);    
  pinMode(inpin, INPUT);
  delay(3500);
}

void loop() {
 begin_time = millis();
 Serial.println(begin_time);
 attachInterrupt(inpin, calculate_speed, RISING); 

 Serial.print(wind_speed);   //m/S
 Serial.println("m/s");
 Serial.println("---------");
 Serial.println(begin_time);
 
}

void calculate_speed(){
  medition_time = millis();
  if(begin_time == 0){
    begin_time = medition_time;
    return;
  }
  float delta = medition_time - begin_time;
  float angular = 3.14159 / delta;
  wind_speed = angular * 0.07;
  begin_time = medition_time;
}

