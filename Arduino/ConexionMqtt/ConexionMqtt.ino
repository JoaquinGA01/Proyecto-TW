#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "iGarcia";
const char* password = "AInEk2020";
const char* mqtt_server = "192.168.0.49";
const char* mqtt_topic = "hola";
const char* mqtt_username = "mjproyect";
const char* mqtt_password = "gA11lEO1";

const int focoPin = 22;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(focoPin, OUTPUT);

  Serial.begin(115200);
  setupWiFi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  reconnect();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void setupWiFi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conexión WiFi establecida");
  Serial.println("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando al servidor MQTT...");
    if (client.connect("ESP32Client", mqtt_username, mqtt_password)) {
      Serial.println("Conectado");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("Falló, rc=");
      Serial.print(client.state());
      Serial.println(" Intentando de nuevo en 5 segundos");
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido en el tópico: ");
  Serial.println(topic);

  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Mensaje: ");
  Serial.println(message);

  if (message == "1") {
    digitalWrite(focoPin, HIGH);
    Serial.println("Foco encendido");
  } else {
    digitalWrite(focoPin, LOW);
    Serial.println("Foco apagado");
  }
}
