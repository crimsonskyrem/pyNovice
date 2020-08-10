import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
car_width = 73

def things(thingx, thingy, thingw, thingh, color):
   pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def message_display(text):
    largeText = pygame.font.SysFont('Hack',115)
    textSurf = largeText.render(text,False,(0,0,0))
    textRect = textSurf.get_rect()
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(2)

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0


thing_startx = random.randrange(0, display_width)
thing_starty = -600
thing_speed = 7
thing_width = 100
thing_height = 100
 

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change
    gameDisplay.fill(white)

    things(thing_startx, thing_starty, thing_width, thing_height, black)
    thing_starty += thing_speed

    car(x, y)

    if x > display_width - car_width or x < 0:
        crashed = True

    pygame.display.update()
    clock.tick(60)

message_display('you crashed')
pygame.quit()