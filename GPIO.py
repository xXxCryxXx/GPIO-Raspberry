
#Beispiel: Taster-Schaltung mit GPIO als Eingangssignal

import RPi.GPIO as GPIO
import random
import time

switch = 17 #Pin anlegen

#GPIO.setmode(GPIO.BOARD) #GPIO Nummerierung nach Pin-Nummerierung auf Board

GPIO.setmode(GPIO.BCM) #GPIO Nummerierung nach GPIO Nummerierung
GPIO.setup(switch, GPIO.IN)# Welcher Pin verwendet werden soll und Eingang oder Ausgang

randomNothing = ["nothing", "still nothing", "just waiting", "Oh! Was there anything? No, probably just a fly", "I'm bored", "I wanna go home"]

try:
    while True:                     #Führe die Zeile 19 bis 23 so lange aus bis sie nicht mehr Wahr ist. 
        if GPIO.input(switch) == 1: #Solange die bedingung Wahr ist bzw. der Schalter betätigt ist
            print("I saw the sign!")#Schreibe in die Console "I saw the sign!"
        else: 
            print(random.choice(randomNothing)) #Wenn keine 1 durch den Schalter erzeugt wird sende random aus der Liste ein Wort
        time.sleep(0.5) # Warte 0,5 Sekunden - 500ms
        
        
except KeyboardInterrupt: #Hier wird der Code durch CTRL + C unterbrochen 
    print("Bye Bye") #Wenn CTRL + C betätigt wurde Schreibe in die Console "Bye Bye"
    GPIO.cleanup() #Cleanup bedeutet das hier die aus und eingänge wieder Stillgelegt werden.