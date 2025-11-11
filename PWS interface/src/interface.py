import serial
import time
import sys
import select
import pygame 
pygame.init()
from bits_naar_string import *
import msvcrt

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
font1 = pygame.font.Font(None,50)
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
    def __init__(self,tekst,x,y,width,hight,typable,status):
        self.text_string = tekst
        self.text = font1.render(self.text_string,True,WHITE)
        self.rect = pygame.Rect((x,y,width,hight))
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.status = status
        self.typable = typable
        self.opgeslagentext = []
        self.file_path = "berichten.txt"
    def draw(self,screen):
        pygame.draw.rect(screen, GRIJS, self.rect)
        screen.blit(self.text,self.text_rect)
    def updatetext(self):
        self.text = font1.render(self.text_string, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.text_rect.w = max(100, text_surface.get_width()+10)
    def opslaan(self):
        central.sendmessages(self.text_string)
        self.opgeslagentext.append(self.text_string)
        with open(self.file_path, "a") as file:
            for tekst in self.opgeslagentext:
                file.write(tekst + "\n")
                #print("txt file was created") Get hastacket LOL!
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
        for button in self.buttons:
            if button.status == True:
                button.draw(screen)
        for sendmessage in self.sendmessage:
            if sendmessage.status == True:
                sendmessage.draw(screen)
    def buttonpress(self, cords): #cycled door elke knop, of deze is geklickt
        for button in self.buttons:
            if (button.rect.collidepoint(cords)):
                button.status = False
    def textboxesUpdate(self,screen):
        if self.buttons[1].status == False:
            self.textboxes[0].status = True #hier mee bezig!
        for textbox in self.textboxes:
            if textbox.status == True:
                textbox.draw(screen)
    def draw(self,screen):
        for textbox in self.textboxes:
            if textbox.status == True:
                textbox.draw(self,screen)
        for sendmessage in self.sendmessage:
            if sendmessage.status == True:
                sendmessage.draw(self,screen)

        for sendmessage in self.sendmessage:
            if sendmessage.status == True:
                sendmessage.draw(self,screen)

    def textboxesChecker(self):
        for textbox in self.textboxes:
            if textbox.status == True:
                return(True)

    def sendmessages(self, tekst):
        central.sendmessage.append(Textbox(tekst,10,self.y,250,100,False,True))
        self.y += 150
        if self.y == 500:
            for sendmessages in self.sendmessage:
                self.y -=150



central = Central()
central.buttons.append(Button("Start", (350, 350, 100,100),True, LBLAUW))
central.buttons.append(Button("type hier", (100, 460, 600,100),True,DGRIJS ))
central.textboxes.append(Textbox("",100, 460, 600,100,True,False))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            central.buttonpress(mouse_position)

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
        
        
        screen.fill(WHITE)

    central.updatebuttons(screen)
    central.textboxesUpdate(screen)
    pygame.display.flip()
    clock.tick(60)


#Buttonlogboek:
# Pos 0: Startknop.
# Pos 1: Typebox test

    #if ser.in_waiting > 0: #als er iets verstuurt is dan leest hij dit. 
        #line = ser.readline().decode('utf-8').strip()
        
        #if line != 'a' and line != 'b':
            #print('string: ' + str(line))
        #else: print('anders'+str(line))

        #text_surface = font1.render(line,True,WHITE)
        #text_rect = text_surface.get_rect(center=(400,300))

    

    #versuurt een string van bits naar het boord
    #if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        #user_input = sys.stdin.readline().strip()
        #ser.write((user_input + "\n").encode())

#Wat moet er nog gedaan worden? Functie in central de een rij van inputs laat zien, met y + 100. met de input moet nog iets worden gedaan.