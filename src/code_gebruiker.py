import serial
import time
import sys
import select
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
font1 = pygame.font.Font(None,50)
text_surface = font1.render('hoi',True,WHITE)
text_rect = text_surface.get_rect(center=(400,300))


# Pas dit aan naar jouw seriële poort:
ser = serial.Serial('/dev/cu.usbserial-14110', 9600, timeout=1)

print('wacht')
time.sleep(3)  # wacht even tot de poort klaar isk
print('klaar')


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
    def __init__(self,tekst,rect,):
        self.text_string = tekst
        self.text = font1.render(self.text_string,True,WHITE)
        self.rect = pygame.Rect(rect)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.status = False
    def draw(self,screen):
        pygame.draw.rect(screen, GRIJS, self.rect)
        screen.blit(self.text,self.text_rect)
    def updatetext(self):
        self.text = font1.render(self.text_string, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)


class Central():
    def __init__(self):
        self.users = []
        self.buttons = []
        self.textboxes = []
    def updatebuttons(self,screen): #Kijkt welke knop getekent moet worden.
        for button in self.buttons:
            if button.status == True:
                button.draw(screen)
    def buttonpress(self, cords): #cycled door elke knop, of deze is geklickt
        for button in self.buttons:
            if (button.rect.collidepoint(cords)):
                button.status = False
    def textboxesUpdate(self,screen):
        if self.buttons[1].status == False:
            self.textboxes[0].draw(screen)
            self.textboxes[0].status = True
    def textboxesChecker(self):
        for textbox in self.textboxes:
            if textbox.status == True:
                return(True)


                

central = Central()
central.buttons.append(Button("Start", (350, 250, 100,100),True, LBLAUW))
central.buttons.append(Button("type hier", (300, 360, 200,100),True,DGRIJS ))
central.textboxes.append(Textbox("", (300, 360, 200,100)))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(ZWART)
    

    if ser.in_waiting > 0: #als er iets verstuurt is dan leest hij dit. 
        line = ser.readline().decode('utf-8').strip()
        
        if line != 'a' and line != 'b':
            print('string: ' + str(line))
        else: print('anders'+str(line))

        text_surface = font1.render(line,True,WHITE)
        text_rect = text_surface.get_rect(center=(400,300))

    

    #versuurt een string van bits naar het boord
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.readline().strip()
        ser.write((user_input + "\n").encode())
        
    screen.blit(text_surface,text_rect)
    pygame.display.flip()
    clock.tick(60)

# alternatieve mainloop, waarin knoppen worden aangemaakt en textboxes.
#while True:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #pygame.quit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #mouse_position = pygame.mouse.get_pos()
            #central.buttonpress(mouse_position)

        #if event.type == pygame.KEYDOWN and central.textboxes[0].status == True:
            #if event.key == pygame.K_BACKSPACE:
                #central.textboxes[0].text_string = central.textboxes[0].text_string[:-1]
            #if event.key == pygame.K_RETURN:
                #central.buttons[1].status = True
                #central.textboxes[0].status = False
            #else:
                #central.textboxes[0].text_string += event.unicode
                #central.textboxes[0].updatetext()
        
        
        #screen.fill(WHITE)

    #central.updatebuttons(screen)
    #central.textboxesUpdate(screen)
    #pygame.display.flip()
    #clock.tick(2)


#Buttonlogboek:
# Pos 0: Startknop.
# Pos 1: Typebox test