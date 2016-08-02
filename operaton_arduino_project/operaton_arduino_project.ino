int port = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(port, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(port, HIGH); // Have pin number 10 always on
  
}
