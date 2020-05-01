from microbit import *
from machine import time_pulse_us
import music
from servo_lib import *


#turn display off, use additional analog pins
display.off()
#Set echo and trig pins
trig = pin2
echo = pin1

trig.write_digital(0)
echo.read_digital()

#setup servo
Servo(pin0).write_angle(0)
sleep(1000)

#create necessary variables for machine logic
my_dist = [] #holds distance readings

Mymusic = [] #holds sequence of notes
loops = 0 #increments to limit how long the machine runs
angle = 0

while True:

    if (button_a.was_pressed()):

        #read light level and select notes
        light = pin3.read_analog()
        print(light) #reporting

        if (light <= 341):
            pos_notes = ['F1:6','G1:6','A1:6','A#1:6','C1:6','D1:6','E1:6',
            'F1:6','G1:6','A1:6','A#1:6','C1:6','r1:2','r1:2','D1:6','E1:6','F1:6','G1:6','A1:6','A#1:6','C1:6','D1:6','E1:6',
            'F1:6','G1:6','A1:6','A#1:6','C1:6','r1:2','r1:2','D1:6','E1:6','F2:6','G2:6','A2:6','A#2:6','C2:6','D2:6','E2:6',
            'F2:6','G2:6','A2:6','A#2:6','C2:6','r1:2','r1:2','D2:6','E2:6','F2:6','G2:6','A2:6','A#2:6','C2:6','D2:6','E2:6',
            'F2:6','G2:6','A2:6','A#2:6','C2:6','r1:2','r1:2','D2:6','E2:6','F3:6','G3:6','A3:6','A#3:6','C3:6','D3:6','E3:6',
            'F3:6','G3:6','A3:6','A#3:6','C3:6','r1:2','r1:2','D3:6','E3:6','F3:6','G3:6','A3:6','A#3:6','C3:6','D3:6','E3:6']
        elif (341 <= light <=682):
            pos_notes = ['A2:4','B2:4','C#2:4','D2:4','E2:4','r1:2','r1:2','F#2:4','G#2:4','A2:4','B2:4','C#2:4','D2:4','E2:4','F#2:4','G#2:4',
            'A2:4','B2:4','C#2:4','D2:4','E2:4','F#2:4','r1:2','r1:2','G#2:4','A2:4','B2:4','C#2:4','D2:4','E2:4','F#2:4','G#2:4',
            'A3:4','B3:4','C#3:4','D3:4','E3:4','F#3:4','r1:2','r1:2','G#3:4','A3:4','B3:4','C#3:4','D3:4','E3:4','F#3:4','G#3:4',
            'A3:4','B3:4','C#3:4','D3:4','E3:4','F#3:4','r1:2','r1:2','G#3:4','A3:4','B3:4','C#3:4','D3:4','E3:4','F#3:4','G#3:4',
            'A4:4','B4:4','C#4:4','D4:4','E4:4','F#4:4','r1:2','r1:2','G#4:4','A4:4','B4:4','C#4:4','D4:4','E4:4','F#4:4','G#4:4',
            'A4:4','B4:4','C#4:4','D4:4','E4:4','F#4:4','r1:2','r1:2','G#4:4','A4:4','B4:4','C#4:4','D4:4','E4:4','F#4:4','G#4:4']
        else:
            pos_notes = ['C2:4','D2:4','E2:4','r1:2','r1:2','F2:4','G2:4','A2:4','B2:4','C2:4','D2:4','E2:4','F2:4','G2:4','A2:4','B2:4',
            'C2:4','D2:4','E2:4','F2:4','G2:4','r1:2','r1:2','A2:4','B2:4','C2:4','D2:4','E2:4','F2:4','G2:4','A2:4','B2:4',
            'C3:4','D3:4','E3:4','F3:4','G3:4','r1:2','r1:2','A3:4','B3:4','C3:4','D3:4','E3:4','F3:4','G3:4','A3:4','B3:4',
            'C3:4','D3:4','E3:4','F3:4','G3:4','r1:2','r1:2','A3:4','B3:4','C3:4','D3:4','E3:4','F3:4','G3:4','A3:4','B3:4',
            'C4:4','D4:4','E4:4','F4:4','G4:4','r1:2','r1:2','A4:4','B4:4','C4:4','D4:4','E4:4','F4:4','G4:4','A4:4','B4:4',
            'C4:4','D4:4','E4:4','F4:4','G4:4','r1:2','r1:2','A4:4','B4:4','C4:4','D4:4','E4:4','F4:4','G4:4','A4:4','B4:4']
        print(pos_notes) #reporting

        while True:

            #ultrasonic setup
            trig.write_digital(1)
            trig.write_digital(0)
            microsec = time_pulse_us(echo, 1)
            time_echo = microsec / 1000000
            dist_cm = (time_echo / 2) * 34300
            dist_inches = dist_cm/2.54
            my_dist = dist_inches

            #normalizing logic to deal with dist measurements beyond 97 inches
            if (my_dist >= 96):
                my_dist = my_dist/8

            #move the servo
            Servo(pin0).write_angle(angle)
            sleep(500)
            print(my_dist) #for reporting
            note = pos_notes[int(my_dist)] #converts my_dist to an INT and then uses that whole number as an index
            print(note) #reporting
            Mymusic.append(note) #appends most recent note to note holder
            print(Mymusic) #reporting
            loops = loops + 1 #increment loops
            angle = angle + 5
            print(loops) #reporting

        #logic to break while loop
            if (loops == 31):
                #play music
                music.play(Mymusic, pin=pin8)
                #reset servo angle for next initialization
                Servo(pin0).write_angle(0)
                #reset tracking variables
                angle = 0
                loops = 0
                break

