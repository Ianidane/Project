import pygame, sys
import random
import threading
from pygame.locals import *
import Main
import textrect
import random
from textrect import *
from Main import *


        
    #Testing for github
    #another test for github
    #bleep

def Event1():
    globalvars.combat = "skirmish"
    globalvars.opopuptxt = "While sailing through the night, you're awakened by noise on the upper deck and the shouts of your fellow sailors. You jump to your feet and prepare for action. When you reach the deck, you can see sailors all scurrying under orders from the captain and an unmarked ship giving chase. You're ordered to man the cannons."
    globalvars.option1txt = "Rush to the cannons and aim for the enemy's hull."
    globalvars.option2txt = "Grab a musket instead and prepare for a possible boarding."
    globalvars.option3txt = "Hide below decks and hope you arn't caught."
    globalvars.eventactive = 2
        
def Event2():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "You notice the trailing ship gaining on you and appears to be within firing range. You aim for the enemy's hull and once given the order, let loose a volley of cannons that make your ears ring."
    globalvars.option1txt = "Continue firing on orders and prepare for close ship combat."
    globalvars.option2txt = "Run above deck and grab a musket and sword to engage."
    globalvars.option3txt = "Hide below decks and hope you arn't caught."
    globalvars.eventactive = 3
        
def Event11():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "After a few volleys and destruction, the ships pull up to each other a few hundred feet away. The damage inflicted from each cannons is devastating, but you choose to retreat back up to the deck to prepare for a possible boarding. Soldiers are already firing at the enemy ship and you file in and join them."
    globalvars.option1txt = "Continue firing."
    globalvars.option2txt = "Hide below decks and hope you arn't caught."
    globalvars.option3txt = "Hide below decks and hope you arn't caught."
    globalvars.eventactive = 4
    
def Event12():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "You continue firing along with your fellow soldiers and sailors at the enemy ship and the figures on it. As the enemy ship pulls up along side yours, the grappling hooks go out and the ships crash together and pirates climb aboard. You're outnumbered but you're serving with Britain's finest in the Royal Navy. Perhaps quality and discipline will win the day."
    globalvars.option1txt = "Fire and reload from a distance."
    globalvars.option2txt = "Charge in with your sword raised high."
    globalvars.option3txt = "It's not too late to hide belowdecks."
    globalvars.eventactive = 5

def Event3():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "As the ships pull up next to each other a few hundred feet away, the damage inflicted from each ship's cannons is devastating. Wooden debris becomes projectiles and keeping concentrated on your task is getting increasingly difficult."
    globalvars.option1txt = "RELOAD. AIM. FIRE."
    globalvars.option2txt = "RELOAD. AIM. FIRE."
    globalvars.option3txt = "Hit the deck and cover yourself for protection."
    globalvars.eventactive = 4
def Event4():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "Both ships taking heavy casualties grind up against each other and all hands are called above deck to ward off the invaders."
    globalvars.option1txt = "Grab a musket and sword and head up to fight."
    globalvars.option2txt = "Remain belowdecks firing your cannon."
    globalvars.option3txt = "It's not too late to hide belowdecks."
    globalvars.eventactive = 5

def Event5():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "You rush to the upper deck where you see pirates swarming your deck and swords clashing. You're clearly outnumbered but you're serving in the British Royal Navy. Will your sailors and troops have the discipline and training to overcome their numbers?"
    globalvars.option1txt = "Charge into the crowd of fighting with your sword raised high."
    globalvars.option2txt = "Fire your weapon from a safe distance."
    globalvars.option3txt = "It's not too late to hide belowdecks."
    globalvars.eventactive = 6
        
def Event6():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "Unfortunately, you and your fellow men are overwhelmed. Men you've been serving with for months are cut down in front of you and your cause is hopeless. You see most of your fellow men throw up their arms in surrender."
    globalvars.option1txt = "Follow the lead of your fellow men and surrender. The day is lost."
    globalvars.option2txt = "Fight to the death. For king and country!"
    globalvars.option3txt = "Take the cowards way out rather than fall prisoner."
    globalvars.eventactive = 0

def Event7():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "You venture above decks against the orders of your captain but your disobedience goes unnoticed in the chaos. You start to load muskets lined along the side of the ship for future confrontation, all the while crashing and screaming can be heard below deck due to the trading of fire."
    globalvars.option1txt = "Continue your task."
    globalvars.option2txt = "Return below deck to follow orders."
    globalvars.option3txt = "Go belowdeck to hide."
    globalvars.eventactive = 8
        
def Event8():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "Men start to come up from below deck to start preparing for closer ship to ship combat. The unidentified ship pulls up along side the HMS success and both ships let loose volleys at once. The destruction is devastating and wood and debris are turned into lethal projectiles. Musketfire rings in your ears as volleys rain over the deck."
    globalvars.option1txt = "Fire on the enemy using the preloaded muskets."
    globalvars.option2txt = "Go belowdeck to hide."
    globalvars.option3txt = "Go belowdeck to hide."
    globalvars.eventactive = 9
        
def Event9():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "As volleys from cannons above and below deck fire off, so do muskets. You can see men from the other ship falling to your musketfire, but your own men are falling as well. Soon the two ships grind up against each other and the pirates attempt to board your ship. You can hear the scrapes of swords clashing and the screams of men dying. You're clearly outnumbered but you're apart of the British Royal Navy. Perhaps your crew's discipline and training will save you."
    globalvars.option1txt = "Charge into the crowd of fighting with your sword raised high."
    globalvars.option2txt = "Continue firing from a safe distance."
    globalvars.option3txt = "It's not too late to go belowdecks."
    globalvars.eventactive = 10

def Event10():
    globalvars.onotclsed = 1
    globalvars.opopuptxt = "You sneak away from the ongoing naval battle and attempt to hide belowdeck."
    globalvars.option1txt = "you're lame"
    globalvars.option2txt = "you're lame"
    globalvars.option3txt = "you're lame"
    globalvars.eventactive = 10
        
def option1():
    if globalvars.eventactive == 2:
        Event2()
      
    
    elif globalvars.eventactive == 3:
        Event3()
      

    elif globalvars.eventactive == 4:
        Event4()
 
        
    elif globalvars.eventactive == 5:
        Event5()


    elif globalvars.eventactive == 6:
        Event6()
        
    elif globalvars.eventactive == 8:
        Event8()
        
    elif globalvars.eventactive == 9:
        Event9()
        
    elif globalvars.eventactive == 10:
        Event6()

def option2():   
    if globalvars.eventactive == 2:
        Event7()
        
    elif globalvars.eventactive == 9:
        Event10()
        
def option3():
    if globalvars.eventactive == 1:
        globalvars.notclsed = 1
        globalvars.popmsg = "You hide below decks and avoid the fighting. Victory can be heard above decks and you have not been caught. You're safe for now."
