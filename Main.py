import pygame, sys
import functions
import globalvars
import threading
from events import *
from time import sleep
from pygame.locals import *
from functions import *
from Tkinter import *



#makes the date move forward
def time():
    global timer
    timer = threading.Timer(0.50, time).start()
    thirtyonemonths = [1, 3, 5, 7, 8, 10, 12]
    thirtymonths = [4, 6, 9, 11]
    if globalvars.ispaused == 0:
        liveseq()
        activity()
        globalvars.day = globalvars.day + 1
        for self in thirtyonemonths:
            if self == globalvars.month:
                if globalvars.day == 32:
                    globalvars.day = 1
                    globalvars.month = globalvars.month + 1
        for self in thirtymonths:
            if self == globalvars.month:
                if globalvars.day == 31:
                    globalvars.day = 1
                    globalvars.month = globalvars.month + 1
        if globalvars.month == 2:
            if globalvars.day == 29:
                globalvars.day = 1
                globalvars.month = globalvars.month + 1
        if globalvars.month == 13:
            globalvars.month = 1
            globalvars.year = globalvars.year + 1

class NameEnter:

	def __init__(self, parent):

		top = self.top = Toplevel(parent)
		Label(top, text="Sailors Name").pack()
		self.e = Entry(top)
		self.e.pack(padx=5)
		b = Button(top, text="OK", command=self.ok)
		b.pack(pady=5)
		

	def ok(self):
		#global SailorName
		print self.e.get()
		#SailorName = self.e.get()
		
		globalvars.SailorName = self.e.get()
		self.top.destroy()
		

root = Tk()
root.withdraw()
root.update()
d = NameEnter(root)
root.wait_window(d.top)
root.destroy


def main():

    print "Hello"
    print globalvars.SailorName
    
    pygame.init()
    globalvars.screen
    globalvars.background
    globalvars.live
    globalvars.inv
    pygame.display.set_caption('Army Project')


    #Main loop
    while True:
        globalvars.screen.blit(globalvars.background, (0,0))
        globalvars.date = str(globalvars.day) + "/" + str(globalvars.month) + "/" + str(globalvars.year)
        #NameEnter().mainloop()
        
        

        
        #pause while popups are open
        if globalvars.notclsed == 1:
            globalvars.ispaused = 1
        if globalvars.onotclsed ==1:
            globalvars.ispaused = 1
        
        #UI
        globalvars.screen.blit(globalvars.mapp, (30, 10))
        functions.info()
        
        #Live button
        b = globalvars.screen.blit(globalvars.live, (965,760))
        pos = pygame.mouse.get_pos()
        if b.collidepoint(pos):
            if globalvars.ispaused == 1:
                globalvars.live = pygame.image.load("images/live2.png").convert_alpha()
        if not b.collidepoint(pos):
            if globalvars.ispaused == 1:
                globalvars.live = pygame.image.load("images/live.png").convert_alpha()
        if b.collidepoint(pos):
            if globalvars.ispaused == 0:
                globalvars.live = pygame.image.load("images/live3.png").convert_alpha()
        if not b.collidepoint(pos):
            if globalvars.ispaused == 0:
                globalvars.live = pygame.image.load("images/live4.png").convert_alpha()


        #Inventory button
        c = globalvars.screen.blit(globalvars.inv, (995,200))
        if c.collidepoint(pos):
            globalvars.inv = pygame.image.load("images/Inv2.png").convert_alpha()
        if not c.collidepoint(pos):
            globalvars.inv = pygame.image.load("images/Inv.png").convert_alpha()
            
        #Activity button
        d = globalvars.screen.blit(globalvars.act, (990,240))
        if d.collidepoint(pos):
            globalvars.act = pygame.image.load("images/Act2.png").convert_alpha()
        if not d.collidepoint(pos):
            globalvars.act = pygame.image.load("images/Act1.png").convert_alpha()
        


        #Activity page open
        if globalvars.anotclsed == 1:
            globalvars.actscrn = globalvars.screen.blit(globalvars.activityscrn, (280,100))
            font = pygame.font.Font("images/mvboli2.ttf", 20)
            font2 = pygame.font.Font("images/mvboli2.ttf", 15)
            font3 = pygame.font.Font("images/mvboli2.ttf", 30)
            
            #Title
            Activity = font3.render("Activity", 1, (1, 1, 1))
            desc = font.render("Please select 2 activities to do in your spare time", 1, (1, 1, 1))
            dispactivity = globalvars.screen.blit(Activity, (520, 130))
            dispdesc = globalvars.screen.blit(desc, (330, 230))
             
            #Options
            globalvars.exitdis = globalvars.screen.blit(globalvars.exitld, (780, 210))
            globalvars.chkptdis = globalvars.screen.blit(globalvars.chkptld, (360, 270))
            globalvars.chkotdis = globalvars.screen.blit(globalvars.chkotld, (580, 270))
            globalvars.chkredis = globalvars.screen.blit(globalvars.chkreld, (360, 325))
            globalvars.chktadis = globalvars.screen.blit(globalvars.chktald, (580, 325))

            #Exit mouseover
            if globalvars.exitdis.collidepoint(pos):
                globalvars.exitld = pygame.image.load("images/exit1.png").convert_alpha()
            if not globalvars.exitdis.collidepoint(pos):
                globalvars.exitld = pygame.image.load("images/exit.png").convert_alpha()

        #3 option popup
        if globalvars.onotclsed == 1:
            font = pygame.font.Font("images/mvboli2.ttf", 12)
            font2 = pygame.font.Font("images/mvboli2.ttf", 15)
            dimensionsopopup = pygame.Rect(globalvars.opopupbox)
            globalvars.opopupscrn = globalvars.screen.blit(globalvars.opopupld, (280,100))
            optionpopuptext = render_textrect(globalvars.opopuptxt, font2, dimensionsopopup, (1,1,1))
            globalvars.screen.blit(optionpopuptext, dimensionsopopup.topleft)
            option1dimensions = pygame.Rect(globalvars.option1blit)
            option2dimensions = pygame.Rect(globalvars.option2blit)
            option3dimensions = pygame.Rect(globalvars.option3blit)
            option1text = render_textrect(globalvars.option1txt, font, option1dimensions, (1,1,1), justification=1)
            option2text = render_textrect(globalvars.option2txt, font, option2dimensions, (1,1,1), justification=1)
            option3text = render_textrect(globalvars.option3txt, font, option3dimensions, (1,1,1), justification=1)
            globalvars.screen.blit(option1text, option1dimensions)
            globalvars.screen.blit(option2text, option2dimensions)
            globalvars.screen.blit(option3text, option3dimensions)
            

            
            
        #Inventory/stats
        if globalvars.inotclsed == 1:
            dimensions3 = pygame.Rect(globalvars.invbox)
            font = pygame.font.Font("images/mvboli2.ttf", 20)
            font2 = pygame.font.Font("images/mvboli2.ttf", 15)
            globalvars.invscrn = globalvars.screen.blit(globalvars.inventoryscrn, (280,100))
            invtext = render_textrect(globalvars.inventorytext, font, dimensions3, (1,1,1))
            globalvars.screen.blit(invtext, dimensions3.topleft)
            globalvars.invbox = globalvars.screen.blit(globalvars.box3, (370, 220))
            

            #non wrapped text
            health = font.render("Health: " + str(globalvars.health), 1, (1, 1, 1))
            sickness = font.render("Sickness: " + globalvars.sickness, 1, (1, 1, 1))
            strength = font.render("Strength: " + str(globalvars.strength), 1, (1, 1, 1))
            stamina = font.render("Stamina: " + str(globalvars.stamina), 1, (1, 1, 1))
            leadership = font.render("Leadership: " + str(globalvars.leadership), 1, (1, 1, 1))
            charisma = font.render("Charisma: " + str(globalvars.charisma), 1, (1, 1, 1))
            dispstamina = globalvars.screen.blit(stamina, (500, 450))
            disphealth = globalvars.screen.blit(health, (420, 140))
            dispsickness = globalvars.screen.blit(sickness, (570, 140))
            dispstrength = globalvars.screen.blit(strength, (360, 450))
            displeadership = globalvars.screen.blit(leadership, (635, 450))
            dispcharisma = globalvars.screen.blit(charisma, (360,500))

        #popups
        if globalvars.notclsed == 1:
            font2 = pygame.font.Font("images/mvboli2.ttf", 15)
            dimensions2 = pygame.Rect(globalvars.popuptxt)
            poptext = render_textrect(globalvars.popmsg, font2, dimensions2, (1,1,1))
            globalvars.pop = globalvars.screen.blit(globalvars.popup, (350,220))
            globalvars.popuptxt = globalvars.screen.blit(globalvars.box2, (410, 285))
            globalvars.screen.blit(poptext, dimensions2.topleft)
            
        #Event Checking
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #Mouse button down
            #Main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if d.collidepoint(pos):
                    print "act"
                    Act()
                if c.collidepoint(pos):
                    print "inv"
                    Inventory()
                if b.collidepoint(pos):
                    if globalvars.firststart == 0:
                        time()
                        globalvars.firststart = 1
                    if globalvars.ispaused == 1:
                        globalvars.ispaused = 0
                        break
                    if globalvars.ispaused == 0:
                        globalvars.ispaused = 1
                        break
                    
                if globalvars.invscrn.collidepoint(pos):
                    if globalvars.inotclsed == 1:
                        if globalvars.notclsed == 0:
                            globalvars.inotclsed = 0
                            
                if globalvars.pop.collidepoint(pos):
                    if globalvars.notclsed == 1:
                        globalvars.ispaused = 0
                        globalvars.notclsed = 0
                        
                #Options popup
                #Option 1 clicked
                if globalvars.option1blit.collidepoint(pos):
                    if globalvars.onotclsed == 1:
                        globalvars.onotclsed = 0
                        option1()
                #Option 2 clicked
                if globalvars.option2blit.collidepoint(pos):
                    if globalvars.onotclsed == 1:
                        globalvars.onotclsed = 0
                        option2()
                #Option 3 clicked
                if globalvars.option3blit.collidepoint(pos):
                    if globalvars.onotclsed == 1:
                        globalvars.onotclsed = 0
                        option3()
                
                #Activity
                if globalvars.exitdis.collidepoint(pos):
                    globalvars.anotclsed = 0
                
                    
                
# **********************************Activity checkmarks*****************************************
                #Physical Training
                if globalvars.chkptdis.collidepoint(pos):
                    if globalvars.anotclsed == 1:
                        if globalvars.ptchecked == 1:
                                globalvars.chkptld = pygame.image.load("images/pt1.png").convert_alpha()
                                globalvars.ptchecked = 0
                                globalvars.checkcount = globalvars.checkcount - 1
                                break
                        if globalvars.checkcount < 2:
                            if globalvars.ptchecked == 0:
                                globalvars.chkptld = pygame.image.load("images/pt2.png").convert_alpha()
                                globalvars.ptchecked = 1
                                globalvars.checkcount = globalvars.checkcount + 1
                                break
                
                        
                #Officer Training  
                if globalvars.chkotdis.collidepoint(pos):
                    if globalvars.anotclsed == 1:
                        if globalvars.otchecked == 1:
                                globalvars.chkotld = pygame.image.load("images/ot1.png").convert_alpha()
                                globalvars.otchecked = 0
                                globalvars.checkcount = globalvars.checkcount - 1
                                break
                        if globalvars.checkcount < 2:
                            if globalvars.otchecked == 0:
                                globalvars.chkotld = pygame.image.load("images/ot2.png").convert_alpha()
                                globalvars.otchecked = 1
                                globalvars.checkcount = globalvars.checkcount + 1
                                break

                #Rest
                if globalvars.chkredis.collidepoint(pos):
                    if globalvars.anotclsed == 1:
                        if globalvars.rechecked == 1:
                                globalvars.chkreld = pygame.image.load("images/re1.png").convert_alpha()
                                globalvars.rechecked = 0
                                globalvars.checkcount = globalvars.checkcount - 1
                                break
                        if globalvars.checkcount < 2:
                            if globalvars.rechecked == 0:
                                globalvars.chkreld = pygame.image.load("images/re2.png").convert_alpha()
                                globalvars.rechecked = 1
                                globalvars.checkcount = globalvars.checkcount + 1
                                break

                #Talking
                if globalvars.chktadis.collidepoint(pos):
                    if globalvars.anotclsed == 1:
                        if globalvars.tachecked == 1:
                                globalvars.chktald = pygame.image.load("images/ta1.png").convert_alpha()
                                globalvars.tachecked = 0
                                globalvars.checkcount = globalvars.checkcount - 1
                                break
                            
                        if globalvars.checkcount < 2:
                            if globalvars.tachecked == 0:
                                globalvars.chktald = pygame.image.load("images/ta2.png").convert_alpha()
                                globalvars.tachecked = 1
                                globalvars.checkcount = globalvars.checkcount + 1
                                break

                
                        
                


            
                        
                

        
        
        pygame.display.update()

if __name__ == '__main__': main()
    
                        




                        






    
