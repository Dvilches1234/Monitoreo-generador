int in_pin = 2;
int revs = 0;
int medition_time = 2000;
int next_medition;
bool last_state = false;  //false --> LOW true --> HIGH
float pi = 3.14159;
float r = 0.07;
float wind_speed;

void setup()
{
  Serial.begin(9600);
  pinMode(in_pin, INPUT);
  digitalWrite(in_pin, LOW);
  next_medition = millis() + medition_time;
  
}  
  
void loop ()
{
  int time = millis();
  if (digitalRead(in_pin) == HIGH){
    if (last_state == false)
      revs++;
    last_state = true; 
  }else{
    last_state = false;
  }
  if (time >= next_medition){
    calculate_speed();
    Serial.println(wind_speed);
    next_medition += medition_time;
  }

}


void calculate_speed(){
   int delta = medition_time /1000;
   float angular = revs * pi /delta;
   wind_speed = angular * r * 3.6;
   revs = 0;
}
