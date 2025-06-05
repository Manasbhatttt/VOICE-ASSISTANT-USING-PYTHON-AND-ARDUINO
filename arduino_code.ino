const int ledPin = 13;  // Built-in LED on most Arduino boards

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for serial port to connect. Needed for native USB
  }
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // Remove any whitespace or newlines

    if (command == "on led") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    } else if (command == "off led") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    } else {
      Serial.println("Unknown command: " + command);
    }
  }
}
