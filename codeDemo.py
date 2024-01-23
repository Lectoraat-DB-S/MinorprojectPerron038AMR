#dit is de code voor station 2 (blauwe band dichts bij zuidberg), dit wordt gebruikt om kratjes te transporteren tussen de genisis en het station zelf

import RPi.GPIO as GPIO
from time import sleep
import requests, json

GPIO.setmode(GPIO.BCM)                               # gebruik BCM GPIO nummers  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # GPIO17 = knop1, blauw, halen, kom een stuk halen van op het station
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # GPIO22 = knop2, groen, brengen, breng een stuk naar het station
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # GPIO10 = eindeloopschakelaar 

a = 158 #random getal dat niet 1 van de 2 toestanden is

#GET request
ip = "10.38.4.15"
host = "http://" + ip + "/api/v2.0.0/"

#headers formatteren
headers = {"Content-Type": "application/json", "Authorization": "Basic ZGlzdHJpYnV0b3I6YjBhOGMwNzI4MzM4YjU0ZGRiYjBkODNkNzk4ZWI2OWY3MWY3YjkyOWViYzY2YTgxNzQxMTc1MWI1YjZkZmNlZA=="}
get_missions = requests.get(host + "missions", headers = headers)


try:  
    while True: # blijft gaan tot CTRL+C  
        if (GPIO.input(17) == 0) and (GPIO.input(10) == 0) and ((a == 0) or (a == 158)): #station wilt van zijn stuk af
            print ("Knop1 is hoog, led1 aan, station wilt nieuw stuk hebben") 
            mission_id = {"mission_id": "c6b4dfa5-b3ab-11ee-8df0-000129ad3d71"} # guid van missie "MissieDemo2_halen"
            post_mission = requests.post(host + "mission_queue", json = mission_id, headers = headers)
            GPIO.output(4, 0) 
            a = 1
        else:
            GPIO.output(4,1)
            sleep (0.2)

        if (GPIO.input(22) == 0) and (GPIO.input(10) == 1) and ((a == 1) or (a == 158)): #station wilt een nieuwe bak
            print ("Knop2 is hoog, led2 aan, station wilt af van zijn doos")
            mission_id = {"mission_id": "1ae5de78-b3ba-11ee-8df0-000129ad3d71"} # guid van missie "MissieDemo2_brengen"
            post_mission = requests.post(host + "mission_queue", json = mission_id, headers = headers)
            GPIO.output(27, 0) 
            a = 0
        else:
            GPIO.output(27,1)
            sleep (0.2)

finally: 
    GPIO.cleanup() 
