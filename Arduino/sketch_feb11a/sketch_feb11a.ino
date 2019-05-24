

///*
//  Blink
//  Turns on an LED on for one second, then off for one second, repeatedly.
// 
//  This example code is in the public domain.
// */
// 
//// Pin 13 has an LED connected on most Arduino boards.
//// give it a name:

int buttonApin = 13;
int buttonBpin = 1;

int led = 12;
int led2 = 11;
int led3 = 10;
int led4 = 9;
int led5 = 8;
int win = 7;
int led6 = 6;
int led7 = 5;
int led8 = 4;
int led9 = 3;
int led10 = 2;


int PWMpin = 10;
//// the setup routine runs once when you press reset:
void setup() {                
//  // initialize the digital pin as an output.

  pinMode(buttonApin, INPUT_PULLUP);  
  pinMode(buttonBpin, INPUT_PULLUP);

  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT); 
  pinMode(led3, OUTPUT);    
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(win, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  pinMode(led9, OUTPUT);
  pinMode(led10, OUTPUT);
}
//
//// the loop routine runs over and over again forever:
void loop() {
  
//  if (digitalRead(buttonApin) == LOW)
//  {
    digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
    delay(50);               // wait for a second
  
    digitalWrite(led2, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led2, LOW);    // turn the LED off by making the voltage LOW
    delay(50); 
  
    digitalWrite(led3, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led3, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led4, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led4, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led5, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led5, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(win, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    

    if (digitalRead(buttonBpin) == LOW)
    {
//      for (int i=0; i <= 3;){
        for (int i=0; i <= 10;){
          digitalWrite(led, HIGH);
          digitalWrite(led2, HIGH);
          digitalWrite(led3, HIGH);
          digitalWrite(led4, HIGH);
          digitalWrite(led5, HIGH);
          digitalWrite(win, HIGH);
          digitalWrite(led6, HIGH);
          digitalWrite(led7, HIGH);
          digitalWrite(led8, HIGH);
          digitalWrite(led9, HIGH);
          digitalWrite(led10, HIGH);
          delay(200);
          //----------------------
          digitalWrite(led, LOW);
          digitalWrite(led2, LOW);
          digitalWrite(led3, LOW);
          digitalWrite(led4, LOW);
          digitalWrite(led5, LOW);
          digitalWrite(win, LOW);
          digitalWrite(led6, LOW);
          digitalWrite(led7, LOW);
          digitalWrite(led8, LOW);
          digitalWrite(led9, LOW);
          digitalWrite(led10, LOW);
          i++;
//        i++;
      }
    }
    digitalWrite(win, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led6, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led6, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led7, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led7, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led8, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led8, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led9, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led9, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led10, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led10, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led9, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led9, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led8, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led8, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led7, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led7, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led6, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led6, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(win, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    

    if (digitalRead(buttonBpin) == LOW)
    {
//      for (int i=0; i <= 3;){
        for (int i=0; i <= 10;){
          digitalWrite(led, HIGH);
          digitalWrite(led2, HIGH);
          digitalWrite(led3, HIGH);
          digitalWrite(led4, HIGH);
          digitalWrite(led5, HIGH);
          digitalWrite(win, HIGH);
          digitalWrite(led6, HIGH);
          digitalWrite(led7, HIGH);
          digitalWrite(led8, HIGH);
          digitalWrite(led9, HIGH);
          digitalWrite(led10, HIGH);
          delay(200);
          //----------------------
          digitalWrite(led, LOW);
          digitalWrite(led2, LOW);
          digitalWrite(led3, LOW);
          digitalWrite(led4, LOW);
          digitalWrite(led5, LOW);
          digitalWrite(win, LOW);
          digitalWrite(led6, LOW);
          digitalWrite(led7, LOW);
          digitalWrite(led8, LOW);
          digitalWrite(led9, LOW);
          digitalWrite(led10, LOW);

      }
    }
    digitalWrite(win, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led5, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led5, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led4, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led4, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led3, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led3, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
  
    digitalWrite(led2, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);               // wait for a second
    digitalWrite(led2, LOW);    // turn the LED off by making the voltage LOW
    delay(50);
}
