import pygame
import time
import random

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

width, height = pygame.display.get_window_size()

deltaT = 0.0
lastT = 0.0
clock = pygame.time.Clock()


def tick():
    global deltaT, lastT
    deltaT = time.time() - lastT
    lastT = time.time()


class Ball:

    def __init__(self, acc):
        self.xPos = width / 2
        self.yPos = height / 2
        self.xVelocity = 0
        self.yVelocity = -1000
        self.yAcceleration = acc
        self.boardPos = width / 2
        self.boardVelocity = 0
        self.boardMovement = 0
        self.isMoving = False

    def update(self):
        self.yVelocity += self.yAcceleration * deltaT
        self.yPos += self.yVelocity * deltaT
        self.xPos += self.xVelocity * deltaT
        self.boardVelocity += self.boardMovement * deltaT
        self.boardPos += self.boardVelocity * deltaT
        if not self.isMoving:
            self.boardVelocity *= 1 - (3 * deltaT)
        self.collision()
        tick()

    def animate(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.xPos, self.yPos, 50, 50))
        pygame.draw.rect(screen, (255, 255, 255), (self.boardPos, height - 100, 300, 30))

    def getKeys(self):
        global running
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.boardMovement = -3000
                    self.isMoving = True
                if event.key == pygame.K_RIGHT:
                    self.boardMovement = 3000
                    self.isMoving = True
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.boardMovement = 0
                    self.isMoving = False

    def collision(self):
        if (self.boardPos <= self.xPos <= self.boardPos + 300) or (self.boardPos <= self.xPos+50 <= self.boardPos + 300):
            if height - 100 <= self.yPos + 50 <= height - 100 + 30:
                self.yVelocity = -self.yVelocity
                self.xVelocity += random.randint(-300, 300)

        if 0 >= self.xPos or self.xPos + 50 >= width:
            self.xVelocity = -self.xVelocity

        if 0 > self.boardPos:
            self.boardPos = 0
            self.boardVelocity = -self.boardVelocity * .3

        if self.boardPos + 300 > width:
            self.boardPos = width - 300
            self.boardVelocity = -self.boardVelocity * .3


running = True
ball = Ball(1000)
tick()
tick()
timme = time.time() + 1
while running:
    screen.fill((120, 120, 120))

    ball.update()
    ball.animate()
    ball.getKeys()

    pygame.display.flip()
