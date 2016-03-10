import time, urllib, StudentClass, naoqi
from StudentClass import Student
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from datetime import datetime
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=OMAR\SQlEXPRESS;'
                                'Database=NAO_Robot;'
                                'uid=;pwd=')

cursor = connection.cursor()
query = "Select * from opleiding where opleidingid = 1"
cursor.execute(query)
results = cursor.fetchone()
print(str(results[0]))
results = cursor.fetchone()
connection.close()

ip = ""
port = 9559

#ALAutonomousLifeProxy = ALProxy("ALAutonomousLifeProxy", ip, port)
ALDarknessThresholdProxy = ALProxy("ALDarknessDetection" , ip, port)
ALMemoryProxy = ALProxy("ALMemory", ip, port)
ALPostureProxy = ALProxy("ALRobotPosture", ip, port)
ALSpeechRecognitionProxy = ALProxy("ALSpeechRecognitionProxy", ip, port)
ALTextTospeechProxy = ALProxy("ALTextTospeechProxy", ip, port)

runProgram = True
studentList = [Student]

#def getStudentMood(student):

#def getAmountOfPeopleInRoom():

#def getNoiseVolume():

def greetStudent():
    currentTime = int(datetime.now().strftime('%H'))
    greeting = ""
    if currentTime < 13:
        greeting = "Good morning, "
    elif currentime > 16:
        greeting = "Good evening, "
    else:
        greeting = "Good afternoon, "     
    say(greeting) #Voeg nog naam van geïdentificeerde student toe.


def makePeopleQuiet():
    # Sounddetection: http://doc.aldebaran.com/1-14/naoqi/audio/alsounddetection-api.html
    say("Sshhhhh")


def makePeopleQuiet():
   say("Sshhhhh")


def say(text):
    ALTextTospeechProxy.say(text)
    return

def startUp():
    ALTextTospeechProxy.setLanguage("English")

def shutDown():
    ALPostureProxy.goToPosture("sit")

def main():
    while(runRrogram):