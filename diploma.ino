#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>
#include <EEPROM.h>

#define reseivePin 10
#define transmitePin 11

SoftwareSerial mySerial(reseivePin, transmitePin);
DFRobotDFPlayerMini myDFPlayer;

const int photoResistors[7] = {2, 3, 4, 5, 6, 7, 8};

int folderNumber;
int state;

void setup() {
    Serial.begin(9600);
    mySerial.begin(9600);
    
    folderNumber = EEPROM.read(0);
    if (folderNumber < 1 || folderNumber > 99) {
        folderNumber = 1;
    }
    state = folderNumber;  

    if (!myDFPlayer.begin(mySerial)) {
        Serial.println("DFPlayer error!");
    }

    myDFPlayer.volume(30);

    for (int i = 0; i < 7; i++) {
        pinMode(photoResistors[i], INPUT);
    }
}

void loop() {
    if (Serial.available() > 0) {
        int inputNumber = Serial.parseInt();
        if (inputNumber >= 1 && inputNumber <= 99) {
            folderNumber = inputNumber;
        }
    }
    
    if (folderNumber != state) {
        state = folderNumber;
        EEPROM.write(0, state);
    }
    
    for (int i = 0; i < 7; i++) {
        if (digitalRead(photoResistors[i])) {
            myDFPlayer.playFolder(folderNumber, photoResistors[i] - 1);
        }
    }
}
