
float begin_time = 0;
float medition_time = 0;
float wind_speed = 0;
int inpin = 2;
int in = 0;
void setup() {
  Serial.begin(9600);    
  pinMode(inpin, INPUT);
}

void loop() {
  if (digitalRead(inpin) == HIGH)
    Serial.println("estoy high perra");
 attachInterrupt(digitalPinToInterrupt(2), calculate_speed, RISING); 

 Serial.println(wind_speed);   //m/S
  
}

void calculate_speed(){
  medition_time = millis();
  float delta = medition_time - begin_time;
  float angular = 3.14159 / delta;
  wind_speed = angular * 0.07;
  begin_time = medition_time;
}

