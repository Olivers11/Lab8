#include <OneWire.h>                
#include <DallasTemperature.h>
#define green_led 8
#define blue_led 7
float last_status = 0.0;
int counter = 0;

int isHigher(int temperature, int reference){
  return temperature + 2 == reference;
}

int isLower(int temperature, int reference){
  return temperature - 2 == reference;
}


void blink_led(int pin){
  digitalWrite(pin, HIGH);
  delay(100);
  digitalWrite(pin, LOW);
  digitalWrite(pin, HIGH);
  delay(100);
  digitalWrite(pin, LOW);
  digitalWrite(pin, HIGH);
  delay(100);
  digitalWrite(pin, LOW);
}


OneWire ourWire(2);               
DallasTemperature sensors(&ourWire); 

void setup() {
  delay(1000);
  Serial.begin(9600);
  sensors.begin();   
  pinMode(green_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
}
 
void loop() {
  sensors.requestTemperatures(); 
  float temp= sensors.getTempCByIndex(0); 
  if(isHigher((int)temp, (int)last_status)){
    blink_led(green_led);
  }
  else if(isLower((int)temp, (int)last_status)){
    blink_led(blue_led);
  }
  Serial.println(temp);

  if(counter == 2){
    last_status = temp;
  }
  counter++;
  
   
  delay(100);    
}
