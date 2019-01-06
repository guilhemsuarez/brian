import pgzrun
from random import randint
import math

# Liste des boutons
myButtons = []
myButtons.append(Actor('redunlit',bottomright=(400,270)))
myButtons[0].state = False
myButtons.append(Actor('greenunlit',bottomleft=(400,270)))
myButtons[1].state = False
myButtons.append(Actor('blueunlit',topright=(400,270)))
myButtons[2].state = False
myButtons.append(Actor('yellowunlit',topleft=(400,270)))
myButtons[3].state = False
playButton = Actor('play', pos=(400,540))
# image des boutons
buttonsLit = ['redlit', 'greenlit', 'bluelit', 'yellowlit']
buttonsUnlit = ['redunlit', 'greenunlit', 'blueunlit', 'yellowunlit']

# Séquence de boutons à cliquer
buttonList = []
playPosition = 0
playingAnimation = False
LOOPDELAY = 80


# Pygame  Zero Draw function
def draw():
    screen.fill((0,210,210))
    for b in myButtons: b.draw()
    playButton.draw()


# Pygame Zero update function
def update():
    global myButons, playingAnimation, playPosition
    if playingAnimation:""
        playPosition += 1
        listPos = math.floor(playPosition/LOOPDELAY)
        if listPos == len(buttonList):
            playingAnimation = False
            clearButtons()
        else:
            litbutton = buttonList[listPos]
            if playPosition%LOOPDELAY > LOOPDELAY/2: litbutton = -1
            bcount = 0
            for b in myButtons:
                if litbutton == bcount: b.state = True
                else: b.state = False
                bcount += 1

    bcount = 0
    for b in myButtons:
        if b.state == True: b.image = buttonsLit[bcount]
        else: b.image = buttonsUnlit[bcount]
        bcount += 1


# Gestion de la souris
def on_mouse_down(pos):
    global myButtons
    for b in myButtons:
        if b.collidepoint(pos): b.state = True


def on_mouse_up(pos):
    global myButtons
    for b in myButtons: b.state = False


def clearButtons():
    global myButtons
    for b in myButtons: b.state = False


def playAnimation():
    global playPosition, playingAnimation
    playPosition = 0
    playingAnimation = True


def addButton():
    global buttonList
    buttonList.append(randint(0, 3))
    playAnimation()


addButton()
addButton()
addButton()
pgzrun.go()    
