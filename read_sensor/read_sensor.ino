#include <OneWire.h>                
#include <DallasTemperature.h>
OneWire ourWire(2);               
 
DallasTemperature sensors(&ourWire); 

void setup() {
  delay(1000);
  Serial.begin(9600);
  sensors.begin();  
}
 
void loop() { 
  sensors.requestTemperatures();   
  float temp= sensors.getTempCByIndex(0); 
  Serial.println(temp);
  delay(100);    
}
