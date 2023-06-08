#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "iGarcia";
const char* password = "AInEk2020";
const char* mqttServer = "192.168.0.2";
const int mqttPort = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

const int pin22 = 22;
const int pin23 = 23;

void setup_wifi() {
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
  Serial.println("WiFi conectado");
  Serial.println("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

void canal1_callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Mensaje recibido en el canal 1");
  if (payload[0] == '1') {
    digitalWrite(pin22, HIGH);  // Activa el pin 22
  } else if (payload[0] == '0') {
    digitalWrite(pin22, LOW);  // Desactiva el pin 22
  }
}

void canal2_callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Mensaje recibido en el canal 2");
  if (payload[0] == '1') {
    digitalWrite(pin23, HIGH);  // Activa el pin 23
  } else if (payload[0] == '0') {
    digitalWrite(pin23, LOW);  // Desactiva el pin 23
  }
}

void canal3_callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Mensaje recibido en el canal 3");
  // Agrega aquí el código que deseas ejecutar cuando se reciba un mensaje en el canal 3
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando al servidor MQTT...");

    if (client.connect("ESP32Client")) {
      Serial.println("Conectado");
      client.subscribe("foco");
      client.subscribe("puerta");
      client.subscribe("canal3");
    } else {
      Serial.print("Fallo, código de error: ");
      Serial.print(client.state());
      Serial.println(" Intentando de nuevo en 5 segundos");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqttServer, mqttPort);
  client.setCallback([](char* topic, byte* payload, unsigned int length) {
    if (strcmp(topic, "foco") == 0) {
      canal1_callback(topic, payload, length);
    } else if (strcmp(topic, "puerta") == 0) {
      canal2_callback(topic, payload, length);
    } else if (strcmp(topic, "canal3") == 0) {
      canal3_callback(topic, payload, length);
    }
  });

  pinMode(pin22, OUTPUT);
  pinMode(pin22, LOW);
  pinMode(pin23, OUTPUT);
  pinMode(pin23, LOW);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
