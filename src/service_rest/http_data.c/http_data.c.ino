#include <ArduinoJson.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>

#define DHTPIN 15 // Pin connected to the DHT sensor (D15)
#define DHTTYPE DHT11 // Type of DHT sensor (DHT11 or DHT22)
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "IL D Wifi";
const char* password = "12345678";
const char* serverName = "http://0.0.0.0:8000/api/";

void setup() {
  dht.begin();
  Serial.begin(9600);
  Serial.println("DHT sensor initialized.");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();         
  
  Serial.print("Humidity: ");
  Serial.print(hum);
  Serial.print("%, Temperature: ");
  Serial.print(temp);
  Serial.println("°C");
 
  // Sending values to the Web server
  WiFiClient client;
  HTTPClient http;
  DynamicJsonDocument jsonDoc(200);
  jsonDoc["temp"] = temp;
  jsonDoc["hum"] = hum;
  String jsonStr;
  serializeJson(jsonDoc, jsonStr);
  
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(jsonStr);

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response Code: ");
    Serial.println(httpResponseCode);
  } else {
    Serial.println("HTTP Request failed.");
  }
  
  http.end();

  // Waiting for 10 seconds before reading the next values
  delay(10000);
}
