
#Beispiel: Taster-Schaltung mit GPIO als Eingangssignal

import RPi.GPIO as GPIO
import random
import time
import matplotlib.pyplot as plt                              #Grafik Plot
import os


def Plot_Value_of_Sensor(input_sensor):
    plt.plot(input_sensor)
    plt.ylabel("Wert Sensor")
    plt.show()


switch = 17 #Pin anlegen
input_sensor = 27 # Eingang
os.system('cls' if os.name == 'nt' else 'clear')
#GPIO.setmode(GPIO.BOARD) #GPIO Nummerierung nach Pin-Nummerierung auf Board

GPIO.setmode(GPIO.BCM)                                       #GPIO Nummerierung nach GPIO Nummerierung
GPIO.setup(switch, GPIO.IN)                                  # Welcher Pin verwendet werden soll und Eingang oder Ausgang
GPIO.setup(input_sensor,GPIO.IN)                             #Sensor (noch offen)
sensorValue0 = GPIO.input(input_sensor)                      #Wert vom Sensor in eine Variable übergeben
sensorValue1 = GPIO.input(switch)
counter = 1

randomNothing = ["nothing", "still nothing", "just waiting", "Oh! Was there anything? No, probably just a fly", "I'm bored", "I wanna go home"]
try:
    while True:                                              # Führe die Zeile 19 bis 23 so lange aus bis der Schalter geschlossen ist 0 = geschlossen. 
        if GPIO.input(switch) == 1:                          # Solange der Schalter geöffnet ist 1 = offen
            print("I saw the sign!")                         # Schreibe in die Console "I saw the sign!"
            Plot_Value_of_Sensor(sensorValue0)              # Hier wird der Wert vom Sensor an die Plott Funktion übergeben.
            if sensorValue0 <= 1:                            # Wenn der Wert kleiner oder gleich 1 ist dann printe den Wert (Nur zum Test)
                print(f"Wert von Sensor0: {sensorValue0}\tWert von Sensor1: {sensorValue1}\n\t Schleife durchlaufen:{counter}") #F_string printout String mit Wert
                counter += 1
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

        else: 
            print(random.choice(randomNothing))              #Wenn keine 1 durch den Schalter erzeugt wird sende random aus der Liste ein Wort
        #time.sleep(0.5)                                      # Warte 0,5 Sekunden - 500ms       

except KeyboardInterrupt:                                    #Hier wird der Code durch CTRL + C unterbrochen 
    print("Bye Bye")                                         #Wenn CTRL + C betätigt wurde Schreibe in die Console "Bye Bye"
    GPIO.cleanup()                                           #Cleanup bedeutet das hier die aus und eingänge wieder Stillgelegt werden.
