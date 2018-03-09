
int analogPin0 = 0;     // potentiometer wiper (middle terminal) connected to analog pin 0
int analogPin1 = 1;     // potentiometer wiper (middle terminal) connected to analog pin 1
int analogPin2 = 2;     // potentiometer wiper (middle terminal) connected to analog pin 2
                       // outside leads to ground and +5V
float val[] ={0,0,0};           // variable to store the value read

void setup()
{
  Serial.begin(9600);              //  setup serial
}
//ON means sound is ON. 
void loop()
{
  val[0] = analogRead(analogPin0);     // read the input pin
  val[1] = analogRead(analogPin1);     // read the input pin
  val[2] = analogRead(analogPin2);     // read the input pin


  if (val[0] < 850)
{
  Serial.print("OFF");
  Serial.print(",");
}
  if (val[0] > 850)
{
  Serial.print("ON");
  Serial.print(",");
}
  if (val[1] < 850)
{
  Serial.print("OFF");
  Serial.print(",");
}
  if (val[1] > 850)
{
  Serial.print("ON");
  Serial.print(",");
}
  if (val[2] < 850)
{
  Serial.println("OFF");
}
  if (val[2] > 850)
{
  Serial.println("ON");
}   



//  Serial.print(val[0]);
//  Serial.print(",");
//  Serial.print(val[1]);
//  Serial.print(",");
//  Serial.println(val[2]);
//  
  /*
  if (val > 850)
  {
    Serial.println("ON");
  }
  if (val < 850)
  {
    Serial.println("OFF");
  }
  */
}
