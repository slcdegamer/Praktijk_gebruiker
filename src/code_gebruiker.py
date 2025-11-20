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


bericht = False
print('wacht')
time.sleep(3)  # wacht even tot de poort klaar isk
print('klaar')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(ZWART)
    

    if ser.in_waiting > 0: #als er iets verstuurt is dan leest hij dit. 
        line = ser.readline().decode('utf-8').strip()
        
        if bericht == True:
            #woord1=(bits_naar_string(line,ascii_naar_woord))
            print(200)
            bericht = False
            text_surface = font1.render(line,True,WHITE)
        text_rect = text_surface.get_rect(center=(400,300))
        if line =='Bericht': 
            bericht = True
            print(100)
        
        if line != '00000000':
            print(line)
        

    #versuurt een string van bits naar het boord
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.readline().strip()
        ser.write((user_input + "\n").encode())
        
    screen.blit(text_surface,text_rect)
    pygame.display.flip()
    clock.tick(60)
