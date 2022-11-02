# all kinds of background music: https://www.chosic.com/download-audio/28509/

# Illusory Realm by Darren Curtis | https://www.darrencurtismusic.com/
# Music promoted on https://www.chosic.com/
# Creative Commons Attribution 3.0 Unported (CC BY 3.0)
# https://creativecommons.org/licenses/by/3.0/

import random
import pygame
import sys
import time
from menuBoxes import menuBox, menuSlider
from generateMap import generateWorld

pygame.init()
pygame.mixer.init()

frames_per_second = 0
clockEnabled = True
difficulty = 0

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

bg = pygame.image.load("background.png").convert()

clickSound = pygame.mixer.Sound("click.wav")
backgroundMusic = pygame.mixer.Sound("Illusory-Realm-MP3.mp3")

clickSound.set_volume(1)
backgroundMusic.set_volume(1)

width, height = pygame.display.get_surface().get_size()
bg = pygame.transform.scale(bg, (width + 100, height + 100))
first = True
tileY, tileX = 54, 96  # rects = 20*20
tiles = -1
while tiles == -1:
    tiles = generateWorld(tileX, tileY)
soundLoudness = 1.00
musicLoudness = 1.00
sliderButtonPressed = [False, False]
lampOnRightNow = False
startTime = 0
lampOnGlobal = False
lampBattery = 100
lampBatteryDrawage = 1

playerPosX = 1000
playerPosY = 0
goingX = 0
goingY = 0
t_ms = time.time()/1000
multiplier = .5
wPressed = False
aPressed = False
sPressed = False
dPressed = False
shiftPressed = False
ctrlPressed = False
indexPos = tiles.index(2)


def loadSettings():
    global clockEnabled, frames_per_second, difficulty, soundLoudness, musicLoudness, clickSound, lampBatteryDrawage
    settings = open("settings.txt", "r")
    settingArray = settings.readlines()[0].split("$")
    settings.close()
    clockEnabled = bool(int(settingArray[0]))
    frames_per_second = int(settingArray[1])
    difficulty = int(settingArray[2])
    soundLoudness = float(settingArray[3])
    musicLoudness = float(settingArray[4])
    lampBatteryDrawage = float(settingArray[5])
    clickSound.set_volume(soundLoudness)
    backgroundMusic.set_volume(musicLoudness)


loadSettings()
backgroundMusic.play(-1)


def saveSettings():
    global frames_per_second, clockEnabled, difficulty, soundLoudness, musicLoudness
    settings = open("settings.txt", "r+")
    settings.truncate(0)
    settings.write(str(int(clockEnabled)))
    settings.write("$")
    settings.write(str(int(frames_per_second)))
    settings.write("$")
    settings.write(str(int(difficulty)))
    settings.write("$")
    settings.write(str(float(soundLoudness)))
    settings.write("$")
    settings.write(str(float(musicLoudness)))
    settings.write("$")
    settings.write(str(float(lampBatteryDrawage)))
    settings.close()


def exitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


def frameCounter():
    global clockEnabled
    if clockEnabled:
        pygame.draw.rect(screen, (100, 100, 100), (width - 50, 25, 25, 25))
        myfont = pygame.font.SysFont('arial', 20)
        frameNumber = myfont.render(str(int(clock.get_fps())), False, (0, 255, 0))
        screen.blit(frameNumber, (width - 46, 26))


def showMap():
    global tiles, tileY, tileX, lampOnGlobal
    while 1:
        clock.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if lampOnGlobal:
                        lampStart()
                    mainGame()
                if event.key == pygame.K_m:
                    if lampOnGlobal:
                        lampStart()
                    mainGame()
        for i in range(tileY):
            for f in range(tileX):
                if tiles[(i * tileX) + f] == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (f * 20, i * 20, 20, 20), 0)
                elif tiles[(i * tileX) + f] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (f * 20, i * 20, 20, 20), 0)
                elif tiles[(i * tileX) + f] == 2:
                    pygame.draw.rect(screen, (0, 255, 0), (f * 20, i * 20, 20, 20), 0)
                elif tiles[(i * tileX) + f] == 3:
                    pygame.draw.rect(screen, (255, 0, 0), (f * 20, i * 20, 20, 20), 0)
        frameCounter()
        pygame.display.flip()


def generalKeys():
    global wPressed, aPressed, sPressed, dPressed, shiftPressed, ctrlPressed, lampOnGlobal
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if lampOnGlobal:
                    lampStop()
                startMenu()
            if event.key == pygame.K_m:
                if lampOnGlobal:
                    lampStop()
                showMap()
            if event.key == pygame.K_h:
                if lampOnGlobal:
                    lampStop()
                else:
                    lampStart()
                lampOnGlobal = not lampOnGlobal
                checkLampState()
            if event.key == pygame.K_LSHIFT:
                shiftPressed = True
            if event.key == pygame.K_LCTRL:
                ctrlPressed = True
            if event.key == pygame.K_w:
                wPressed = True
            if event.key == pygame.K_a:
                aPressed = True
            if event.key == pygame.K_s:
                sPressed = True
            if event.key == pygame.K_d:
                dPressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shiftPressed = False
            if event.key == pygame.K_LCTRL:
                ctrlPressed = False
            if event.key == pygame.K_w:
                wPressed = False
            if event.key == pygame.K_a:
                aPressed = False
            if event.key == pygame.K_s:
                sPressed = False
            if event.key == pygame.K_d:
                dPressed = False


def loading():
    count = 0
    alphaFade = 0
    while 1:
        exitCheck()
        count += random.randint(0, 5)
        clock.tick(frames_per_second)
        screen.fill((0, 0, 0))
        x, y = pygame.mouse.get_pos()
        screen.blit(bg, (-100 + (float(x) / width * 100), -100 + (float(y) / height * 100)))
        pygame.draw.rect(screen, (70, 70, 70), (100, height - 50, width - 200, 30))
        pygame.draw.rect(screen, (220, 220, 220), (100, height - 50, count, 30))
        frameCounter()
        pygame.display.flip()
        if count >= 1720:
            time.sleep(1.5)
            while alphaFade < 255:
                s = pygame.Surface((width, height))  # the size of your rect
                s.set_alpha(int(alphaFade))  # alpha level
                s.fill((0, 0, 0))  # this fills the entire surface
                screen.blit(s, (0, 0))
                alphaFade += 4
                frameCounter()
                pygame.display.flip()
            time.sleep(1)
            break


def startMenu():
    global bg, first
    alphaFade = 0
    if first:
        alphaFade = 255
        first = False
    bg = pygame.transform.scale(bg, (width, height))
    while 1:
        startMenuCheckMouse()
        exitCheck()
        clock.tick(frames_per_second)
        screen.fill((0, 0, 0))
        clock.tick(frames_per_second)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        menuBox(screen, width / 2 - 150, height / 2 - 50, 300, 100, "Start")
        menuBox(screen, width - 250, height - 150, 200, 100, "Options")
        if difficulty == 0:
            menuBox(screen, width / 2 - 225, height - 150, 450, 100, "Difficulty: Easy")
        if difficulty == 1:
            menuBox(screen, width / 2 - 225, height - 150, 450, 100, "Difficulty: Moderate")
        if difficulty == 2:
            menuBox(screen, width / 2 - 225, height - 150, 450, 100, "Difficulty: Hard")
        frameCounter()
        menuBox(screen, 25, 25, 100, 50, "Quit")
        if alphaFade > 0:
            s = pygame.Surface((width, height))  # the size of your rect
            s.set_alpha(int(alphaFade))  # alpha level
            s.fill((0, 0, 0))  # this fills the entire surface
            screen.blit(s, (0, 0))
            alphaFade -= 5
        pygame.display.flip()


def drawBattery(window, batCharge, batX, batY, batWidth, batHeight, batColor):
    pygame.draw.lines(window, batColor, True,
                      ((batX + batWidth * .3, batY), (batX + batWidth * .7, batY), (batX + batWidth * .7,
                                                                                    batY + batHeight * .05),
                       (batX + batWidth, batY + batHeight * .05), (batX + batWidth, batY + batHeight), (batX, batY +
                                                                                                        batHeight),
                       (batX, batY + batHeight * .05), (batX + batWidth * .3, batY + batHeight * .05)))
    pygame.draw.rect(window, batColor, (
        batX, batY + batHeight - ((batHeight * .95) * (batCharge / 100)), batWidth + 1, batHeight * (batCharge / 100)))


def mainGame():
    global frames_per_second, lampBattery, playerPosX, playerPosY,  t_ms, wPressed, aPressed, sPressed, dPressed, goingY, goingX, shiftPressed, ctrlPressed, multiplier, indexPos
    while 1:
        generalKeys()

        if lampOnGlobal:
            screen.fill((125, 125, 125))
        else:
            screen.fill((0, 0, 0))

        drawTiles(screen, playerPosX, playerPosY, indexPos, tiles)

        clock.tick(frames_per_second)
        checkLampState()

        if lampOnGlobal:
            drawBattery(screen, lampBattery - (time.time() - startTime)*lampBatteryDrawage, 1720, 820, 75, 150, (255, 255, 255))
        else:
            drawBattery(screen, lampBattery, 1720, 820, 75, 150, (255, 255, 255))

        if aPressed and dPressed or not aPressed and not dPressed:      # Movement (wasd, shift, control)
            goingX = 0
        elif aPressed:
            goingX = -1
        elif dPressed:
            goingX = 1
        if wPressed and sPressed or not wPressed and not sPressed:
            goingY = 0
        elif wPressed:
            goingY = -1
        elif sPressed:
            goingY = 1
        if ctrlPressed and shiftPressed or not ctrlPressed and not shiftPressed:
            multiplier = .5
        elif ctrlPressed:
            multiplier = .15
        elif shiftPressed:
            multiplier = 1
        if aPressed or dPressed:
            playerPosX += (goingX*multiplier)*((time.time()/1000-t_ms)*1000000)
        if wPressed or sPressed:
            playerPosY += (goingY*multiplier)*((time.time()/1000-t_ms)*1000000)
        t_ms = time.time()/1000

        if playerPosY > 2000:      # roll over or something, idk
            playerPosY = 1
            if tiles[indexPos + tileX] != 0:
                indexPos += tileX
            else:
                playerPosY = 2000
        if playerPosY < 0:
            playerPosY = 2000
            if tiles[indexPos - tileX] != 0:
                indexPos -= tileX
            else:
                playerPosY = 0
        if playerPosX > 2000:
            playerPosX = 1
            if tiles[indexPos + 1] != 0:
                indexPos += 1
            else:
                playerPosX = 2000
        if playerPosX < 0:
            playerPosX = 2000
            if tiles[indexPos - 1] != 0:
                indexPos -= 1
            else:
                playerPosX = 0

        pygame.draw.rect(screen, (125, 125, 125), (int(width/2), int(height/2), 50, 50))
        pygame.draw.circle(screen, (0, 0, 0), (int(width/2), int(height/2)), 1)
        frameCounter()
        pygame.display.flip()


def drawTiles(window, playPosX, playPosY, index, world):
    if world[index] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY, 2000, 2000))
    if world[index] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX, int(height/2)-playPosY, 2000, 2000))
    if world[index] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX, int(height/2)-playPosY, 2000, 2000))
    if world[index] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY, 2000, 2000))

    if world[index+1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY, 2000, 2000))
    if world[index+1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX+2000, int(height/2)-playPosY, 2000, 2000))
    if world[index+1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY, 2000, 2000))
    if world[index+1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY, 2000, 2000))

    if world[index-1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY, 2000, 2000))
    if world[index-1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX-2000, int(height/2)-playPosY, 2000, 2000))
    if world[index-1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY, 2000, 2000))
    if world[index-1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY, 2000, 2000))

    if world[index+tileX] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY+2000, 2000, 2000))

    if world[index+tileX+1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX+1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX+2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX+1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX+1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY+2000, 2000, 2000))

    if world[index+tileX-1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX-1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX-2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX-1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY+2000, 2000, 2000))
    if world[index+tileX-1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY+2000, 2000, 2000))

    if world[index-tileX] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX, int(height/2)-playPosY-2000, 2000, 2000))

    if world[index-tileX+1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX+1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX+2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX+1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX+1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX+2000, int(height/2)-playPosY-2000, 2000, 2000))

    if world[index-tileX-1] == 0:
        pygame.draw.rect(window, (0, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX-1] == 1:
        pygame.draw.rect(window, (255, 255, 255), (int(width/2)-playPosX-2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX-1] == 2:
        pygame.draw.rect(window, (0, 255, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY-2000, 2000, 2000))
    if world[index-tileX-1] == 3:
        pygame.draw.rect(window, (255, 0, 0), (int(width/2)-playPosX-2000, int(height/2)-playPosY-2000, 2000, 2000))


def startMenuCheckMouse():
    global difficulty, lampOnGlobal, lampBatteryDrawage

    if pygame.mouse.get_pressed(3)[0] and width / 2 - 150 <= pygame.mouse.get_pos()[0] <= width / 2 + 150 and height \
            / 2 - 50 <= pygame.mouse.get_pos()[1] <= height / 2 + 50:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if lampOnGlobal:
            lampStart()
        mainGame()

    if pygame.mouse.get_pressed(3)[0] and 25 <= pygame.mouse.get_pos()[0] <= 125 and 25 <= pygame.mouse.get_pos()[1] \
            <= 75:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        saveSettings()
        clickSound.play()
        time.sleep(0.08)
        sys.exit()

    if pygame.mouse.get_pressed(3)[0] and width - 250 <= pygame.mouse.get_pos()[0] <= width - 50 and height - 150 <= \
            pygame.mouse.get_pos()[1] <= height - 50:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        options()

    if pygame.mouse.get_pressed(3)[0] and width / 2 - 225 <= pygame.mouse.get_pos()[
        0] <= width / 2 + 225 and height - 150 <= \
            pygame.mouse.get_pos()[1] <= height - 50:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if difficulty == 0:
            difficulty = 1
            lampBatteryDrawage = 1
            saveSettings()
            return
        if difficulty == 1:
            difficulty = 2
            lampBatteryDrawage = 2
            saveSettings()
            return
        if difficulty == 2:
            difficulty = 0
            lampBatteryDrawage = .5
            saveSettings()
            return


def options():
    global bg, soundLoudness, musicLoudness
    bg = pygame.transform.scale(bg, (width, height))
    while 1:
        optionsCheckMouse()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loadSettings()
                    startMenu()
        clock.tick(frames_per_second)
        screen.fill((0, 0, 0))
        clock.tick(frames_per_second)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        if clockEnabled:
            menuBox(screen, 150, 100, 450, 100, "Show FPS counter: ON")
        if not clockEnabled:
            menuBox(screen, 150, 100, 450, 100, "Show FPS counter: OFF")
        if frames_per_second == 5000:
            menuBox(screen, 150, 300, 450, 100, "FPS: unl.")
        if frames_per_second == 75:
            menuBox(screen, 150, 300, 450, 100, "FPS: 75")
        if frames_per_second == 60:
            menuBox(screen, 150, 300, 450, 100, "FPS: 60")
        if frames_per_second == 30:
            menuBox(screen, 150, 300, 450, 100, "FPS: 30")
        menuBox(screen, width - 250, height - 150, 200, 100, "Back")
        menuBox(screen, width - 500, height - 150, 200, 100, "Save")
        menuSlider(screen, 150, 500, 1000, 20, soundLoudness, sliderButtonPressed[0], "Sound")
        menuSlider(screen, 150, 600, 1000, 20, musicLoudness * 5, sliderButtonPressed[1], "Music")
        frameCounter()
        pygame.display.flip()


def optionsCheckMouse():
    global clockEnabled, frames_per_second, soundLoudness, sliderButtonPressed, musicLoudness
    if pygame.mouse.get_pressed(3)[0] and width - 250 <= pygame.mouse.get_pos()[0] <= width - 50 and height - 150 <= \
            pygame.mouse.get_pos()[1] <= height - 50:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if width - 250 <= pygame.mouse.get_pos()[0] <= width - 50 and height - 150 <= pygame.mouse.get_pos()[1] \
                <= height - 50:  # back
            loadSettings()
            startMenu()

    if pygame.mouse.get_pressed(3)[0] and width - 500 <= pygame.mouse.get_pos()[0] <= width - 300 and height - 150 <= \
            pygame.mouse.get_pos()[1] <= height - 50:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if width - 500 <= pygame.mouse.get_pos()[0] <= width - 300 and height - 150 <= pygame.mouse.get_pos()[1] \
                <= height - 50:  # save
            saveSettings()
            startMenu()

    if pygame.mouse.get_pressed(3)[0] and 150 <= pygame.mouse.get_pos()[0] <= 600 and 100 <= \
            pygame.mouse.get_pos()[1] <= 200:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if 150 <= pygame.mouse.get_pos()[0] <= 600 and 100 <= pygame.mouse.get_pos()[1] <= 200:
            clockEnabled = not clockEnabled

    if pygame.mouse.get_pressed(3)[0] and 150 <= pygame.mouse.get_pos()[0] <= 600 and 300 <= \
            pygame.mouse.get_pos()[1] <= 400:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        clickSound.play()
        if 150 <= pygame.mouse.get_pos()[0] <= 600 and 300 <= pygame.mouse.get_pos()[1] <= 400:
            if frames_per_second == 30:
                frames_per_second = 60
                return
            if frames_per_second == 60:
                frames_per_second = 75
                return
            if frames_per_second == 75:
                frames_per_second = 5000
                return
            if frames_per_second == 5000:
                frames_per_second = 30
                return

    if sliderButtonPressed[0] and not pygame.mouse.get_pressed(3)[0]:
        clickSound.set_volume(soundLoudness)
        clickSound.play()
    if int(150 - 10 + (1000 * soundLoudness)) <= pygame.mouse.get_pos()[0] <= int(150 - 10 + (1000 * soundLoudness)) + \
            20 and pygame.mouse.get_pressed(3)[0] and 500 - 20 <= pygame.mouse.get_pos()[1] <= 500 + 20 or \
            sliderButtonPressed[0] and pygame.mouse.get_pressed(3)[0]:
        sliderButtonPressed[0] = True
        soundLoudness = (pygame.mouse.get_pos()[0] - 150) / 1000
        if soundLoudness <= 0:
            soundLoudness = 0
        elif soundLoudness >= 1:
            soundLoudness = 1
    else:
        sliderButtonPressed[0] = False

    if sliderButtonPressed[1] and not pygame.mouse.get_pressed(3)[0]:
        backgroundMusic.set_volume(musicLoudness)
    if int(150 - 10 + (1000 * (musicLoudness * 5))) <= pygame.mouse.get_pos()[0] <= \
            int(150 - 10 + (1000 * (musicLoudness * 5))) + 20 and pygame.mouse.get_pressed(3)[0] and 600 - 20 <= \
            pygame.mouse.get_pos()[1] <= 600 + 20 or sliderButtonPressed[1] and pygame.mouse.get_pressed(3)[0]:
        sliderButtonPressed[1] = True
        musicLoudness = (pygame.mouse.get_pos()[0] - 150) / 5000
        if musicLoudness <= 0:
            musicLoudness = 0
        elif musicLoudness >= 0.2:
            musicLoudness = 0.2
        backgroundMusic.set_volume(musicLoudness)
    else:
        sliderButtonPressed[1] = False


def lampStop():
    global lampOnRightNow, startTime, lampBattery
    timeRan = time.time() - startTime
    lampBattery -= timeRan * lampBatteryDrawage
    lampOnRightNow = False


def lampStart():
    global startTime, lampOnRightNow, lampBattery
    if lampBattery > 0:
        startTime = time.time()
        lampOnRightNow = True


def checkLampState():
    global lampOnGlobal
    if (time.time() - startTime)*lampBatteryDrawage >= lampBattery and lampOnGlobal:
        lampOnGlobal = False
        lampStop()


# loading()
startMenu()
