float input_voltage = 0.0;
float intensity = 0;
float res = 1340 ;
void setup()
{
   Serial.begin(9600);     //  opens serial port, sets data rate to 9600 bps
 }
void loop()
{

   
   int analog_value = analogRead  (A1);
   input_voltage = (analog_value * 5.0) / 1024.0; 

   
  /* if (input_voltage < 0.02) 
   {
     input_voltage=0.0;
   }
   */
  intensity = input_voltage * 100000/ res;
    Serial.print("I= ");
    Serial.println(intensity,4);
    delay(1000);
}

          
