#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

#define reseivePin 0;
#define transmitePin 1;
SoftwareSerial mySerial(reseivePin, transmitePin);
DFRobotDFPlayerMini myDFPlayer;

const int photoResistors[7] = {2, 3, 4, 5, 6, 7, 8};

int folderNumber = 1;

void setup() {
    Serial.begin(9600);
    mySerial.begin(9600);

    if (!myDFPlayer.begin(mySerial)) {
        Serial.println("DFPlayer error!");
        while (true);
    }

    myDFPlayer.volume(20);

    for (int i = 0; i < 7; i++) {
        pinMode(photoResistors[i], INPUT);
    }
}

void loop() {
    if (Serial.available()) {
        int newFolder = Serial.parseInt();
        if (newFolder >= 1 && newFolder <= 99) {
            folderNumber = newFolder;
        }
    }

    for (int i = 0; i < 7; i++) {
        if (digitalRead(photoResistors[i]) == LOW) {
            myDFPlayer.playFolder(folderNumber, i + 1);
            delay(350);
        }
    }

    delay(300);
}
