# Room Music Generator
Microbit Device that makes music based on the room it is in.

### Build Instructions
This device is built using the Keyestudio 37 in 1 kit for the BBC Micro:bit. All sensors needed for this device can be found in that kit.

This device uses:
1 Microbit
1 V2 sensor shield
1 HC-SR04 Ultrasonic Module
1 Keyestudio Passive Buzzer module
1 TEMT6000 Ambient Light Sensor
1 Micro Servo
1 Premium Battery Case 6-cell AA
10 F-F Dupont Jumper Wires

To build this device, plug the microbit into the V2 sensor shield and change the voltage jumpers to 5 volt.

Plug the servo wires into the zero row of pins on the sensor shield with the yellow wire connected to the S column, red to v column, brown to the ground.

Plug the ultrasonic sensor echo into S1 and the trig into S2. Plug VCC into V2, and ground into a free ground pin.

Plug ambient light sensor S pin into S3 on the sensor shield, the + pin into a V3, the - pin into a free ground pin.

Plug passive buzzer pin S into S8 on the sensor shield, the + into V4, the - pin into a free ground pin.

Plug the battery case into the servo shield. 

### Flash and install software
Using a microUSB cable and Mu Editor Software, plug the microbit into the usb and flash Room_music_V0.5FF.py 
Download the servo_lib.py and place it in Mu Editor folder
When the microbit lights up with a line four error, drag the servo library file into the microbit. Now your Room Music Generator shoudl work! 

Press the A button on the microbit to start the device. When it's done playing music, press A to do it again!

