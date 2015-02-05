import pygame, sys
import random
from events import *
import threading
from pygame.locals import *
import Main
import textrect
from textrect import *
from Main import *


        
    

def info():

    #Date
    font = pygame.font.Font("images/mvboli2.ttf", 20)
    font2 = pygame.font.Font("images/mvboli2.ttf", 15)
    text = font.render("Date: " + str(globalvars.day) + "/" + str(globalvars.month) + "/" + str(globalvars.year), 1, (1, 1, 1))
    dispinf = globalvars.screen.blit(text, (980, 90))

<<<<<<< HEAD
    #Main Scroll
    textbox = globalvars.screen.blit(globalvars.box, (130, 560))
    dimensions = pygame.Rect(textbox)
    scroll = render_textrect(globalvars.scrolllog, font2, dimensions, (1,1,1))
    if scroll:
        globalvars.screen.blit(scroll, dimensions.topleft)
=======
>>>>>>> d36233e470c2370a81384b9106dc4906cf6cdc53

def Act():
    globalvars.anotclsed = 1

def liveseq():
    print random.random()
    if globalvars.date == "1/1/1803":
        globalvars.notclsed = 1
    if globalvars.date == "7/1/1803":
        globalvars.notclsed = 1
        globalvars.popmsg = "The actions you take in the future are directly related to your statistics and the activities you do in your spare time."
    if random.random() < .005:
        globalvars.notclsed = 1
        globalvars.popmsg = "As the days pass by, you can feel yourself getting older"
        globalvars.health = globalvars.health - 1
    if random.random() < .30:
		if globalvars.Event1flagged == 0:
			globalvars.onotclsed = 1
			globalvars.option1 = 1
			Event1()
        
    
    
def Inventory():
    globalvars.inotclsed = 1
                
            
        


    


def activity():
    if globalvars.ptchecked == 1:
        if globalvars.day == 1:
            globalvars.strength = globalvars.strength + 1
            globalvars.stamina = globalvars.stamina + 0.5

    if globalvars.otchecked == 1:
        if globalvars.day == 1:
            globalvars.leadership = globalvars.leadership + .6
            globalvars.charisma = globalvars.charisma + 0.2

    if globalvars.rechecked == 1:
        if globalvars.day == 1:
            if globalvars.health < 100:
                globalvars.health = globalvars.health + 1

    if globalvars.tachecked == 1:
        if globalvars.day == 1:
            globalvars.charisma = globalvars.charisma + 1
            globalvars.leadership = globalvars.leadership + 0.2
            


                

