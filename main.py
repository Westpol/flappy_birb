'''
Background Music:

Monkeys Spinning Monkeys Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 3.0 License
http://creativecommons.org/licenses/by/3.0/
Music promoted by https://www.chosic.com/free-music/all/
'''

import pygame
import time
import random

PG_INITIALIZED = False
width = 0
height = 0
FPS = 1
screen = pygame.display.set_mode((0, 0))
clock = pygame.time.Clock()
deltaT = 0
lasttime = 0
pipeWidth = 75
circle_radius = 20
highscore = 0

pg_events = pygame.event.get()


def collision():
    print(birb.vPos)
    if birb.score > highscore:
        with open("score.txt", "w") as scoreFile:
            scoreFile.write(str(birb.score))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                exit_check(event)


def physics_tick():
    global lasttime, deltaT
    deltaT = time.time() * 1000 - lasttime
    lasttime = time.time() * 1000


def factor():
    return deltaT / 10


def exit_check(evnt):
    if evnt.key == pygame.K_ESCAPE:
        menu.menuToggle()
        exit()


def init_check():
    if PG_INITIALIZED:
        return 0
    raise Exception("pg_init not called at the beginning of the code.")


def pg_init(windowMode, setWidth: int, setHeight: int, setFPS: int):
    global screen, width, height, FPS, PG_INITIALIZED, clock, highscore

    pygame.init()
    pygame.mixer.init()
    FPS = setFPS
    clock = pygame.time.Clock()
    if windowMode == pygame.FULLSCREEN:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    elif windowMode is None:
        screen = pygame.display.set_mode((setWidth, setHeight))
    else:
        raise ValueError(
            "Window Mode not correctly set. Try 'None' for windowed mode and 'pygame.FULLSCREEN' for fullscreen Mode")
    width, height = screen.get_size()

    print("initializing Window")
    print(f"Specs:")
    if windowMode == pygame.FULLSCREEN:
        print("Mode: Fullscreen")
    else:
        print("Mode: Windowed")
    print("Window Dimensions: {0} x {1}".format(width, height))
    PG_INITIALIZED = True
    with open("score.txt", "r") as highscoreFile:
        highscore = int(highscoreFile.read())


def updating_window():
    global screen, clock
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(FPS)


class Birb:

    def __init__(self, acc):
        global height, width, screen
        init_check()
        self.vPos = height / 2
        self.hPos = width / 2.5
        self.vel = 0
        self.acc = acc
        self.score = 0

    def update(self):
        self.vel += self.acc * factor()
        self.vPos += self.vel * factor()
        #self.vel += self.acc
        #self.vPos += self.vel

    def animate(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.hPos, self.vPos), circle_radius)

    def collision_detection(self):
        if 0 > self.vPos or self.vPos > height:
            collision()
        for pip in pipes.pipelist:
            if (pip[0] - pipes.pos - circle_radius < self.hPos < pip[0] - pipes.pos + pipeWidth + circle_radius) and (0 < self.vPos < pip[1] + circle_radius):
                collision()
        for pip in pipes.pipelist:
            if (pip[0] - pipes.pos - circle_radius < self.hPos < pip[0] - pipes.pos + pipeWidth + circle_radius) and (pip[1] - circle_radius + pipes.space < self.vPos < height):
                collision()

    def space_pressed(self):
        for event in pg_events:
            if event.type == pygame.KEYDOWN:
                exit_check(event)
                if event.key == pygame.K_SPACE:
                    self.vel = -8
                    s.flapp()


class Pipes:

    def __init__(self, space):
        self.space = space
        self.pos = 0
        self.pipelist = [(width + 200, random.randint(50, height - self.space - 50), False)]
        self.pipeNum = 1
        # pipelist = [x - 1 for x in pipelist]

    def update(self):
        self.pos += 2 * factor()
        self.updateScore()

    def animate(self):
        for pipe in self.pipelist:
            pygame.draw.rect(screen, (255, 255, 255), (pipe[0] - self.pos, 0, pipeWidth, pipe[1]), 0)
            pygame.draw.rect(screen, (255, 255, 255), (pipe[0] - self.pos, pipe[1] + self.space, pipeWidth, height - (pipe[1] + self.space)), 0)

    def setPipes(self):
        if self.pos > self.pipeNum * 300:
            self.pipeNum += 1
            self.pipelist.append((width + self.pipeNum * 300, random.randint(50, height - self.space - 50), False))
            while 1:
                is_oob = (0, False)
                for i in range(len(self.pipelist)):
                    if self.pipelist[i][0] - self.pos < - 500:
                        is_oob = (i, True)
                if is_oob[1]:
                    self.pipelist.pop(is_oob[0])
                else:
                    break

    def updateScore(self):
        for i in range(len(self.pipelist)):
            if birb.hPos > self.pipelist[i][0] - self.pos and not self.pipelist[i][2]:
                self.pipelist[i] = (self.pipelist[i][0], self.pipelist[i][1], True)
                birb.score += 1


class Sound:

    def __init__(self):
        self.sound = pygame.mixer.Sound("sounds/BackgroundMusic.mp3")
        self.flapSound = pygame.mixer.Sound("sounds/flap.wav")

    def backgroundMusic(self):
        self.sound.play()

    def flapp(self):
        self.flapSound.play()


class UI:

    def __init__(self):
        self.arial_40 = pygame.font.SysFont('arial', 40)
        self.arial_20 = pygame.font.SysFont('arial', 20)

    def animate(self):
        x, y, w, h = width/2 - 40, 20, 80, 50   # setting position
        pygame.draw.rect(screen, (220, 220, 220), (x, y, w, h))     # drawing rect for better contrast
        score = self.arial_40.render(str(birb.score), False, (0, 0, 0))     #generating text object
        screen.blit(score, (x, y))  # drawing text object

        x, y, w, h = width - 100, 20, 80, 50
        pygame.draw.rect(screen, (220, 220, 220), (x, y, w, h))
        highscoreText = self.arial_40.render(str(highscore), False, (0, 0, 0))
        screen.blit(highscoreText, (x, y))

    def show_fps(self):
        frameNumber = self.arial_20.render(str(int(clock.get_fps())), False, (0, 255, 0))
        screen.blit(frameNumber, (width - 46, 26))

    class Keys:

        def __init__(self):
            pass

        def getPresses(self):
            pass


class Menu:

    def __init__(self):
        self.menuState = 0
        self.menuActive = True
        self.arial_40 = pygame.font.SysFont('arial', 40)
        self.arial_20 = pygame.font.SysFont('arial', 20)

    def mainMenu(self):
        if self.menuActive:
            whilebrk = True
            while whilebrk:
                self.animate()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            physics_tick()
                            physics_tick()
                            whilebrk = False
                            self.menuToggle()

    def animate(self):
        pipes.animate()
        birb.animate()
        ui.animate()
        self.draw()
        updating_window()

    def draw(self):
        x, y, w, h = width / 2 - 100, height / 2 - 25, 200, 50  # setting position
        pygame.draw.rect(screen, (220, 220, 220), (x, y, w, h))  # drawing rect for better contrast
        score = self.arial_40.render('"p" drücken um fortzufahren', False, (0, 0, 0))  # generating text object
        screen.blit(score, (x, y))  # drawing text object

    def update(self):
        for event in pg_events:
            if event.type == pygame.KEYDOWN:
                exit_check(event)
                if event.key == pygame.K_p:
                    self.menuToggle()
                    self.mainMenu()

    def menuToggle(self):
        self.menuActive = not self.menuActive


if __name__ == '__main__':
    pg_init(pygame.FULLSCREEN, 0, 0, 0)
    s = Sound()
    birb = Birb(0.4)
    pipes = Pipes(175)

    birb.animate()
    updating_window()

    menu = Menu()

    #s.backgroundMusic()

    ui = UI()
    keys = UI.Keys()

    lasttime = time.time() * 1000
    menu.mainMenu()
    while 1:
        pg_events = pygame.event.get()
        physics_tick()

        keys.getPresses()

        menu.update()
        #menu.animate()

        birb.space_pressed()
        birb.update()
        birb.collision_detection()
        birb.animate()

        pipes.update()
        pipes.animate()
        pipes.setPipes()

        ui.animate()
        ui.show_fps()

        updating_window()
