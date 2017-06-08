#define uint  unsigned int

#define ulong unsigned long



#define PIN_ANEMOMETER  2     // Digital 2




// How often we want to calculate wind speed or direction

#define MSECS_CALC_WIND_SPEED 5000





volatile int numRevsAnemometer = 0; // Incremented in the interrupt

ulong nextCalcSpeed;                // When we next calc the wind speed


ulong time;                         // Millis() at each start of loop().



// ADC readings:









byte dirOffset=0;



//=======================================================

// Initialize

//=======================================================

void setup(){
  Serial.println("hey");

  Serial.begin(9600);

  pinMode(PIN_ANEMOMETER, INPUT);

  digitalWrite(PIN_ANEMOMETER, HIGH);

  attachInterrupt(0, countAnemometer, FALLING);

  nextCalcSpeed = millis() + MSECS_CALC_WIND_SPEED;  

}



//=======================================================

// Main loop.

//=======================================================

void loop() {

 //  Serial.println(numRevsAnemometer);

  time = millis();



  if (time >= nextCalcSpeed) {

     calcWindSpeed();

     nextCalcSpeed = time + MSECS_CALC_WIND_SPEED;
     float v = digitalRead(PIN_ANEMOMETER);
     Serial.println(v);

  }

 

}



//=======================================================

// Interrupt handler for anemometer. Called each time the reed

// switch triggers (one revolution).

//=======================================================

void countAnemometer() {

  numRevsAnemometer++;

}



//=======================================================

// Calculate the wind speed, and display it (or log it, whatever).

// 1 rev/sec = 1.492 mph

//=======================================================

void calcWindSpeed() {

  int x, iSpeed;

  // This will produce mph * 10

  // (didn't calc right when done as one statement)

  long speed = 2.4;

  speed *= numRevsAnemometer;

  speed /= MSECS_CALC_WIND_SPEED;

  iSpeed = speed;         // Need this for formatting below



  Serial.print("Wind speed: ");

  x = iSpeed / 10;

  Serial.print(x);

  Serial.print('.');

  x = iSpeed % 10;

  Serial.print(x);



  numRevsAnemometer = 0;        // Reset counter

}
