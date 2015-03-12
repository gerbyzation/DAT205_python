boolean on = false;

void setup() {
    Serial.begin(9600);
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  
 // listen for serial messages 
  if (Serial.available() > 0) {
    char num = Serial.read();
    Serial.print(num);
    if (num == '0') {
      on = false;
      digitalWrite(13, LOW);
    };
    
    if (num == '1') {
      on = true;
      digitalWrite(13, HIGH);
    };
  }  
}
