import pygame
import time
import random

PG_INITIALIZED = False
width = 0
height = 0
FPS = 1
screen = None
clock = None


def init_check():
    print(PG_INITIALIZED)
    if PG_INITIALIZED:
        return 0
    raise Exception("pg_init not called at the beginning of the code.")


def pg_init(windowMode, setWidth: int, setHeight: int, setFPS: int):
    global screen, width, height, FPS, PG_INITIALIZED, clock

    pygame.init()
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

    def update(self):
        self.vel += self.acc
        self.vPos += self.vel

    def animate(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.hPos, self.vPos), 20)

    def collision_detection(self):
        if 0 > self.vPos or self.vPos > height:
            exit()

    def space_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.vel = -8


class Pipes:

    def __init__(self, space):
        self.space = space
        self.pos = 0
        self.pipelist = []
        # pipelist = [x - 1 for x in pipelist]

    def update(self):
        pass

    def animate(self):
        pass


if __name__ == '__main__':
    pg_init(None, 1000, 500, 100)
    birb = Birb(0.4)
    pipes = Pipes(150)

    while 1:
        birb.space_pressed()
        birb.update()
        birb.collision_detection()
        birb.animate()

        updating_window()
