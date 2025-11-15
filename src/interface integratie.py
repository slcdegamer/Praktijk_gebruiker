import time
import sys
import select
import serial
import pygame 
pygame.init()
from bits_naar_string import *


breedte, hoogte = 800, 600
screen = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Mijn eerste Pygame")
clock = pygame.time.Clock()

ZWART= (0,0,0)
WHITE= (255,255,255)
LBLAUW = (0,191,255)
GRIJS = (169,169,169)
DGRIJS = (40,40,40)
#To do: Textbox class, centrale class, systeem met users, chatrooms.
font1 = pygame.font.Font(None,25)
text_surface = font1.render('hoi',True,WHITE)


# Pas dit aan naar jouw seriële poort:
#ser = serial.Serial('COM3', 9600, timeout=1)

#print('wacht')
#time.sleep(3)  # wacht even tot de poort klaar isk
#print('klaar')

class Button:
    def __init__(self, tekst, rect, status, kleur):
        self.tekst = font1.render(tekst,True,WHITE)
        self.rect = pygame.Rect(rect)
        self.text_rect = self.tekst.get_rect(center=self.rect.center)
        self.status = status
        self.kleur = kleur
    def draw(self,screen):
        pygame.draw.rect(screen, self.kleur, self.rect)
        screen.blit(self.tekst,self.text_rect)

class Textbox:
    def __init__(self,tekst,x,y,width,hight,typable,status,color):
        self.text_string = tekst
        self.text = font1.render(self.text_string,True,WHITE)
        self.y = y
        self.rect = pygame.Rect((x,self.y,width,hight))
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.status = status
        self.typable = typable
        self.opgeslagentext = []
        self.file_path = "deberichten.txt"
        self.color = color
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text,self.text_rect)
    def updatetext(self):
        self.text = font1.render(self.text_string, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.text_rect.w = max(100, text_surface.get_width()+10)
    def opslaan(self):
        print("eyyy")
        central.sendmessages(self.text_string,"send")
        self.opgeslagentext.append(self.text_string)
        with open(self.file_path, "a") as file:
            for tekst in self.opgeslagentext:
                file.write(tekst + "\n")
                print("txt file was created")
                self.opgeslagentext = []
        self.text_string = ""


class Central():
    def __init__(self):
        self.users = []
        self.buttons = []
        self.textboxes = []
        self.sendmessage = []
        self.x = 10
        self.y = 50
    def updatebuttons(self,screen): #Kijkt welke knop getekent moet worden.

        for sendmessage in self.sendmessage:
            if sendmessage.status == True:
                sendmessage.draw(screen)
        for button in self.buttons:
            if button.status == True:
                button.draw(screen)
        if self.buttons[1].status == False:
            self.textboxes[0].status = True
        pygame.draw.rect(screen, DGRIJS,(0, 510, 800,600))
        for textbox in self.textboxes:
            if textbox.status == True:
                textbox.draw(screen)
    def buttonpress(self, cords): #cycled door elke knop, of deze is geklickt
        for button in self.buttons:
            if (button.rect.collidepoint(cords)):
                button.status = False
    def textboxesChecker(self):
        for textbox in self.textboxes:
            if textbox.status == True:
                return(True)

    def sendmessages(self, tekst,type):
        if type == "send":
            x = 450
            color = LBLAUW
        else:
            x = 10 
            color = GRIJS
            self.y -=50
        central.sendmessage.append(Textbox(tekst,x,self.y,300,50,False,True,color))
        
        ser.write((string_naar_bits('bericht.'+tekst, woord_naar_ascii) + "\n").encode()) #de regel die de bits naar het bord verstuurt 
        self.y += 100
        if self.y > 500:
           central.movemessages("down") 
           
    def movemessages(self,richting):
            if richting == "down":
                x = 1
            else:
                x = -1
            for msg in self.sendmessage:
                msg.y -= 100*x
                msg.rect.y = msg.y
                msg.text_rect = msg.text.get_rect(center=msg.rect.center)
            self.y -= 100*x



central = Central()
central.buttons.append(Button("Start", (350, 350, 100,100),True, LBLAUW))
central.buttons.append(Button("type hier", (0, 460, 800,50),True,ZWART ))
central.textboxes.append(Textbox("",0, 460, 800,50,True,False,GRIJS))

ser = serial.Serial('/dev/cu.usbserial-14110', 9600, timeout=1)
bericht= False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            central.buttonpress(mouse_position)
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                central.movemessages("up")
            else:
                central.movemessages("down")
        if event.type == pygame.KEYDOWN and central.textboxes[0].status == True:
            if event.key == pygame.K_BACKSPACE:
                central.textboxes[0].text_string = central.textboxes[0].text_string[:-1]
            elif event.key == pygame.K_RETURN:
                central.buttons[1].status = True
                central.textboxes[0].status = False
                central.textboxes[0].opslaan()
            else:
                central.textboxes[0].text_string += event.unicode
            central.textboxes[0].updatetext()
    
    if ser.in_waiting > 0: #als er iets verstuurt is dan leest hij dit. 
        line = ser.readline().decode('utf-8').strip()
        if bericht == True:
            bericht = False 
            
            #als bericht ontvangen via het bordje dan wordt dit testbericht verstuurt
            woord,woord2=bits_naar_string('1000000101010000010111111111',ascii_naar_woord) 
            central.sendmessages(woord,'ding')
            
            # dit hieronder is de echte code 
            #type_bericht,tekst = bits_naar_string(line,ascii_naar_woord)
            #if type_bericht == 'bericht':
                #central.sendmessages(tekst,'ding')

        if line =='Bericht': 
            bericht = True
        
        if line != '00000000':
            print(line)

        screen.fill(WHITE)

    central.updatebuttons(screen)
    pygame.display.flip()
    clock.tick(60)


#Buttonlogboek:
# Pos 0: Startknop.
# Pos 1: Typebox test

