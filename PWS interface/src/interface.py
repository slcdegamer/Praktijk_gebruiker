import time
import sys
import select
import serial
import pygame 
pygame.init()
from berichten_converter import *
#import msvcrt
import serial.tools.list_ports

ports = serial.tools.list_ports.comports() #autodetect welke port
for port in ports:
    port = port.device
#hopelijk werkt dit

breedte, hoogte = 800, 600
screen = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Interface")
clock = pygame.time.Clock()

ZWART= (0,0,0)
WHITE= (255,255,255)
LBLAUW = (0,191,255)
GRIJS = (169,169,169)
DGRIJS = (40,40,40)

font1 = pygame.font.Font(None,25)
text_surface = font1.render('hoi',True,WHITE)

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
    def __init__(self,status_draw,tekst,x,y,width,hight,typable,status,color):
        self.status_draw=status_draw
        self.text_string = tekst
        self.text = font1.render(self.text_string,True,WHITE)
        self.y = y
        self.rect = pygame.Rect((x,self.y,width,hight))
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.status = status
        self.typable = typable
        self.opgeslagentextself = []
        self.opgeslagentextander = []
        self.file_path_verstuur = "deberichten.txt"
        self.file_path2_ontvang = "ontvangenberichten.txt"
        self.color = color
    def draw(self,screen):
        if self.status_draw == True:
            pygame.draw.rect(screen, self.color, self.rect)
            screen.blit(self.text,self.text_rect)
    def updatetext(self):
        self.text = font1.render(self.text_string, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.text_rect.w = max(100, text_surface.get_width()+10)
    def opslaan(self):
        central.sendmessages(self.text_string, "None")
        self.opgeslagentextself.append(self.text_string)
        with open(self.file_path_verstuur, "a") as file:
            for tekst in self.opgeslagentextself:
                file.write(tekst + "\n")
                print("txt file was created")
                self.opgeslagentextself = []
                ser.write((string_naar_bits('bericht.'+tekst, woord_naar_ascii) + "\n").encode()) #de regel die de bits naar het bord verstuurt
                central.huidige_pariteitbit=pariteitbits_gever(string_naar_bits('bericht.'+tekst,woord_naar_ascii))
                print('bericht wordt verstuurd...')
        self.text_string = ""

    def anderekantopslaan(self,tekst):
        self.text_string=tekst
        central.sendmessages(self.text_string, "send")
        self.opgeslagentextander.append(self.text_string)
        with open(self.file_path2_ontvang, "a") as file:
            for tekst in self.opgeslagentextander:
                file.write(tekst + "\n")
                self.opgeslagentextander = []
                
        self.text_string = ""

    def binnengekregentext(self):
        with open(self.file_path2_ontvang, "r") as file2:
            for line in file2:
                if '\n' in line:
                    line = line[:-1]
                central.sendmessages(line, None)
        with open(self.file_path_verstuur, "r") as file2:
            for line in file2:
                if '\n' in line:
                    line = line[:-1]
                central.sendmessages(line, 'inladen')

class Central:
    def __init__(self):
        self.huidige_pariteitbit=''
        self.status_huidig_bericht = False
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
        if self.buttons[0].status == False:
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
            color = GRIJS
            self.y +=50
            central.sendmessage.append(Textbox(False,tekst,x,self.y,300,50,False,True,color))
        elif type == 'inladen':
            x = 450
            color = GRIJS
            self.y +=50
            central.sendmessage.append(Textbox(True,tekst,x,self.y,300,50,False,True,color))
        else:
            x = 10 
            color = LBLAUW
            self.y +=50
            central.sendmessage.append(Textbox(True,tekst,x,self.y,300,50,False,True,color))
        self.y += 10
        if self.y > 500:
           central.movemessages("down") 
           
    def movemessages(self,richting):
            if richting == "down":
                x = 1
            else:
                x = -1
            for msg in self.sendmessage:
                msg.y -= 50*x
                msg.rect.y = msg.y
                msg.text_rect = msg.text.get_rect(center=msg.rect.center)
            self.y -= 50*x



central = Central()

central.buttons.append(Button("type hier", (0, 460, 800,50),True,ZWART ))
central.textboxes.append(Textbox(True,"",0, 460, 800,50,True,False,GRIJS))

central.textboxes[0].binnengekregentext()
ser = serial.Serial(port, 9600, timeout=1) #pas '/dev/tty.usbserial-14110' aan naar je eigen port waar het bordje op zit aangesloten 
time.sleep(2)  # tijd buffer om het bordje ook even op goed te laten inladen 
ser.reset_input_buffer()
bericht= False
bericht_gechecked = True

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Pijltje omhoog ingedrukt!")
                ser.write(('a\n').encode())
            if event.key ==  pygame.K_DOWN:
                ser.write(('b\n').encode())
                print("Pijltje omlaag ingedrukt!")
         
        if event.type == pygame.KEYDOWN and central.textboxes[0].status == True:
            if event.key == pygame.K_BACKSPACE:
                central.textboxes[0].text_string = central.textboxes[0].text_string[:-1]
            elif event.key == pygame.K_RETURN:
                central.buttons[0].status = True
                central.textboxes[0].status = False
                central.textboxes[0].opslaan()
            else:
                central.textboxes[0].text_string += event.unicode
            central.textboxes[0].updatetext()
        
    if ser.in_waiting > 0: #als er iets verstuurt is van het bordje en in de wachtrij staat dan leest het dit 
        line = ser.readline().decode('utf-8').strip()
        if bericht == True:
            bericht = False
            type_bericht,tekst = bits_naar_string(line,ascii_naar_woord)
            
            if  tekst == 'error' and type_bericht != 'check_klopt' and type_bericht != 'check_klopt_niet' or tekst == '' and type_bericht != 'check_klopt' and type_bericht != 'check_klopt_niet':
                print('signaal verkeerd ontvangen...')
                
            if type_bericht == 'bericht' and tekst!= 'error':
                
                if bericht_gechecked == False: # als het vorige bericht nooit gechecked is, dus niet goed ontvangen is, dan wordt de tekst aangepast en laadt het bericht in. 
                    central.sendmessage[-1].status_draw=True
                    central.sendmessage[-1].text=font1.render('bericht niet juist geladen',True,WHITE)
                    text_rect = central.sendmessage[-1].text.get_rect(center=central.sendmessage[-1].rect.center)
               
                central.status_huidig_bericht = False
                central.textboxes[0].anderekantopslaan(tekst)
                time.sleep(1)
                ser.write((string_naar_bits('check_vraag.'+pariteitbits_gever(line), woord_naar_ascii) + "\n").encode())
                print('Bericht ontvangen! check wordt verstuurd')
                bericht_gechecked=False
                
            elif type_bericht == 'check_klopt':
                central.sendmessage[-1].status_draw=True #pas als het binnengekomen bericht correct gechecked is wordt het ingeladen 
                bericht_gechecked = True
                print('Correct bericht ontvangen!')
            elif type_bericht == 'check_klopt_niet':
                central.sendmessage.remove(central.sendmessage[-1])
                bericht_gechecked = True
                print('Fout bericht ontvangen...')
            elif type_bericht == 'check_vraag': #als de ontvangen pariteit bits kloppen met het orginele verzonden bericht, dan is het bericht correct verstuurd 
                time.sleep(1)
                if tekst == central.huidige_pariteitbit: 
                    ser.write((string_naar_bits('check_klopt.', woord_naar_ascii) + "\n").encode())
                    print('Check klopt!')
                else: 
                    ser.write((string_naar_bits('check_klopt_niet.', woord_naar_ascii) + "\n").encode())
                    print('Check klopt niet...')
            
        if line =='Bericht': #als een bericht binnenkort, stuurt de Wemos eerst "Bericht" zodat de interface weet dat het volgende line een bericht is
            bericht = True 
        
        if line != '00000000':
            print(line)

    screen.fill(WHITE)


    central.updatebuttons(screen)
    pygame.display.flip()
    clock.tick(60)


#Buttonlogboek:
# Pos 0: Typebox test

