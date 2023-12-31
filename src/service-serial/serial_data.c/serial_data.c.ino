#include "DHT.h"

#define DHTPIN 15
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  delay(1000);
  
  // Get the current time in milliseconds
  unsigned long currentTime = millis();
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed reception");
    return;
  }

  // Print the elapsed time, humidity, and temperature
  Serial.print(currentTime / 1000); // Convert milliseconds to seconds
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.println(t);
}
