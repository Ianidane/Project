import pygame, sys
import random
import threading
from pygame.locals import *
year = 1803
month = 1
day = 1


date = str(day) + "/" + str(month) + "/" + str(year)
print date

firststart = 0
ispaused = 1

charnames = ["Jack Jefferson", "John MacLean", "Robert Baratheon", "Eric Berd", "David Taleman"]
captnames = ["Captain George Neeson"]

rank = "Shiphand"
currship = "HMS Success"
mission = "Patrol the English Channel"
captain = random.choice(captnames)
charname = random.choice(charnames)


"Ship combat"
combat = "none"
eshiphealth = 100
eshipcrew = 80



"health/stats"
sickness = "none"
health = 100
strength = 1
stamina = 1
leadership = 1
charisma = 1


notclsed = 0
inotclsed = 0
anotclsed = 0
onotclsed = 0

checkcount = 0
ptchecked = 0
otchecked = 0
rechecked = 0
tachecked = 0

"misc stuff"
rect = pygame.Rect(878, 48, 200, 100)
screen = pygame.display.set_mode((1200, 900),0,32)
live = pygame.image.load("images/live.png").convert_alpha()
inv = pygame.image.load("images/Inv.png").convert_alpha()
act = pygame.image.load("images/Act1.png").convert_alpha()
mapp = pygame.image.load("images/map.png").convert_alpha()
background = pygame.image.load("images/back.png").convert_alpha()
box = pygame.image.load("images/box.png").convert_alpha()
checkcount = 0


"popup images"
popup = pygame.image.load("images/popup.png").convert_alpha()
pop = screen.blit(popup, (100,100))
box2 = pygame.image.load("images/box2.png").convert_alpha()
popuptxt = screen.blit(box2, (300,200))
popmsg = "The year is 1803 and Europe is preparing for a massive coalition war against Napoleon. \n You have enlisted as a shiphand aboard the " + str(currship) + " with the British Royal Navy "

"Activity popup"
exitld = pygame.image.load("images/exit.png").convert_alpha()
exitld1 = pygame.image.load("images/exit1.png").convert_alpha()
exitdis = screen.blit(exitld, (500, 100))
activityscrn = pygame.image.load("images/activity.png").convert_alpha()
actscrn = screen.blit(activityscrn, (100,100))

"Activity checkmarks"
chkptld = pygame.image.load("images/pt1.png").convert_alpha()
chkptld2 = pygame.image.load("images/pt2.png").convert_alpha()
chkptdis = screen.blit(chkptld, (300, 200))
chkotld = pygame.image.load("images/ot1.png").convert_alpha()
chkotdis = screen.blit(chkotld, (500, 200))
chkreld = pygame.image.load("images/re1.png").convert_alpha()
chkredis = screen.blit(chkreld, (500, 200))
chktald = pygame.image.load("images/ta1.png").convert_alpha()
chktadis = screen.blit(chktald, (500, 200))

"Option popup"
box4 = pygame.image.load("images/opopuptxtbox.png").convert_alpha()
opopupld = pygame.image.load("images/opopup.png").convert_alpha()
opopupscrn = screen.blit(opopupld, (280,100))
option1 = 1
option2 = 1
option3 = 1
eventactive = 1
opopuptxt = "we like sports and we dont care who knows"
option1txt = "From something"
option2txt = "I"
option3txt = "Michael sucks"
opopupbox = screen.blit(box4, (335, 150))
option1ld = pygame.image.load("images/option1.png").convert_alpha()
option2ld = pygame.image.load("images/option2.png").convert_alpha()
option3ld = pygame.image.load("images/option3.png").convert_alpha()
option1blit = screen.blit(option1ld, (315, 489))
option2blit = screen.blit(option2ld, (315, 529))
option3blit = screen.blit(option3ld, (315, 569))


"Inventory popup"
box3 = pygame.image.load("images/box3.png").convert_alpha()
inventoryscrn = pygame.image.load("images/Inventory.png").convert_alpha()
invscrn = screen.blit(inventoryscrn, (100,100))
invbox = screen.blit(box3, (160, 80))

inventorytext = "                   Inventory \n \n \n \n \n \n                   Statistics"

scrolllog = "1/1/1803 - " + charname + " Enlisted as a shiphand on " + currship + " under " + captain + "\n \n 1/1/1803 - Mission: " + mission + " Issued to " + captain

                        






    
