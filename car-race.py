import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


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

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

    if click[0] == 1 and action != None:
        action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf = smallText.render(msg, False,(0,0,0))
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        textSurf = largeText.render("A bit Racey",False,(0,0,0))
        textRect = textSurf.get_rect()
        textRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(textSurf, textRect)

        button("GO!",150,450,100,50,green,bright_green,gameLoop)
        button("Quit",550,450,100,50,red,bright_red,quitGame)

def quitGame():
    message_display('crashed')
    gameOver = True
    pygame.quit()


def gameLoop():
    gameOver = False
    car_width = 73
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    move = 0
    dodged = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move = -5
                elif event.key == pygame.K_RIGHT:
                    move = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move = 0
        x += move
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            gameOver = True

        if x > display_width - car_width or x < 0:
            message_display('crashed')
            gameOver = True

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                message_display('crashed')
                gameOver = True

        pygame.display.update()
        clock.tick(60)

game_intro()
gameLoop()