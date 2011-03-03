int ledPin = 13;  // choose the pin for the LED
int val = 0;      // variable for reading the pin status
char msg = '  ';   // variable to hold data from serial

void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  Serial.begin(9600);
  Serial.print("Program Initiated\n");
}

void loop(){
        // While data is sent over serial assign it to the msg
	while (Serial.available()>0){
		msg=Serial.read();
	}

  // Turn LED on/off if we recieve 'Y'/'N' over serial
  if (msg=='Y') {
    digitalWrite(ledPin, HIGH);  // turn LED ON
    Serial.print("LED Activated\n");
    msg=' ';
  } else if (msg=='N') {
    digitalWrite(ledPin, LOW); // turn LED OFF
  }
}
