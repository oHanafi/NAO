import time, json, urllib, StudentClass, naoqi
from StudentClass import Student
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from datetime import datetime


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

def pullStudentInfoFromJsonServer(id, params):
    jsonUrl = "http://145.93.78.4:4000/users"
    jsonUrl += "/" + string(id)
    for item in params:
       jsonUrl += ("/" + item)
    return json.loads(jsonUrl)

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

def tellGrades(student Student):

def makePeopleQuiet():
    # Sounddetection: http://doc.aldebaran.com/1-14/naoqi/audio/alsounddetection-api.html
    say("Sshhhhh")

#def getDarknessLevel():
#    lightLevel = ALDarknessThresholdProxy.getDarknessThreshold()
#    print(lightLevel)
#    if(sum(Student.preferredLightLevel for Student in studentList)/studentList.count(Student) < lightLevel):
#        say("Its dark, could someone lighten the area up?")
#    return
#
#def greetStudent():

#def tellGradess(student Student):

def makePeopleQuiet():
   say("Sshhhhh")


def say(text):
    ALTextTospeechProxy.say(text)
    return

def startUp():
    ALTextTospeechProxy.setLanguage("English")

def shutDown():

def main():
    while(runRrogram):
        delay