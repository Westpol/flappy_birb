import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()


def dropdownMenu(pygamescreen, mouseX, mouseY):
    global width, height
    while 1:
        if mouseY + 150 < height:
            pygame.draw.rect(pygamescreen, (200, 0, 0), (mouseX, mouseY, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 200, 0), (mouseX, mouseY+25, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 0, 200), (mouseX, mouseY+50, 75, 25))
            pygame.draw.rect(pygamescreen, (200, 200, 0), (mouseX, mouseY+75, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 200, 200), (mouseX, mouseY+100, 75, 25))
            pygame.draw.rect(pygamescreen, (200, 0, 200), (mouseX, mouseY+125, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY <= pygame.mouse.get_pos()[1] <= mouseY+25:
                pygame.draw.rect(pygamescreen, (255, 0, 0), (mouseX, mouseY, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+25 <= pygame.mouse.get_pos()[1] <= mouseY+50:
                pygame.draw.rect(pygamescreen, (0, 255, 0), (mouseX, mouseY+25, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+50 <= pygame.mouse.get_pos()[1] <= mouseY+75:
                pygame.draw.rect(pygamescreen, (0, 0, 255), (mouseX, mouseY+50, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+75 <= pygame.mouse.get_pos()[1] <= mouseY+100:
                pygame.draw.rect(pygamescreen, (255, 255, 0), (mouseX, mouseY+75, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+100 <= pygame.mouse.get_pos()[1] <= mouseY+125:
                pygame.draw.rect(pygamescreen, (0, 255, 255), (mouseX, mouseY+100, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+125 <= pygame.mouse.get_pos()[1] <= mouseY+150:
                pygame.draw.rect(pygamescreen, (255, 0, 255), (mouseX, mouseY+125, 75, 25))
        else:
            pygame.draw.rect(pygamescreen, (200, 0, 0), (mouseX, mouseY-25, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 200, 0), (mouseX, mouseY-50, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 0, 200), (mouseX, mouseY-75, 75, 25))
            pygame.draw.rect(pygamescreen, (200, 200, 0), (mouseX, mouseY-100, 75, 25))
            pygame.draw.rect(pygamescreen, (0, 200, 200), (mouseX, mouseY-125, 75, 25))
            pygame.draw.rect(pygamescreen, (200, 0, 200), (mouseX, mouseY-150, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-25 <= pygame.mouse.get_pos()[1] <= mouseY:
                pygame.draw.rect(pygamescreen, (255, 0, 0), (mouseX, mouseY-25, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-50 <= pygame.mouse.get_pos()[1] <= mouseY-25:
                pygame.draw.rect(pygamescreen, (0, 255, 0), (mouseX, mouseY-50, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-75 <= pygame.mouse.get_pos()[1] <= mouseY-50:
                pygame.draw.rect(pygamescreen, (0, 0, 255), (mouseX, mouseY-75, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-100 <= pygame.mouse.get_pos()[1] <= mouseY-75:
                pygame.draw.rect(pygamescreen, (255, 255, 0), (mouseX, mouseY-100, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-125 <= pygame.mouse.get_pos()[1] <= mouseY-100:
                pygame.draw.rect(pygamescreen, (0, 255, 255), (mouseX, mouseY-125, 75, 25))
            if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY-150 <= pygame.mouse.get_pos()[1] <= mouseY-125:
                pygame.draw.rect(pygamescreen, (255, 0, 255), (mouseX, mouseY-150, 75, 25))

        pygame.display.flip()
        if pygame.mouse.get_pressed(3)[0]:
            while pygame.mouse.get_pressed(3)[0]:
                pygame.event.pump()
            if mouseY + 150 < height:
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY <= pygame.mouse.get_pos()[1] <= mouseY+25:
                    return 1
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+25 <= pygame.mouse.get_pos()[1] <= mouseY+50:
                    return 2
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+50 <= pygame.mouse.get_pos()[1] <= mouseY+75:
                    return 3
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+75 <= pygame.mouse.get_pos()[1] <= mouseY+100:
                    return 4
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+100 <= pygame.mouse.get_pos()[1] <= mouseY+125:
                    return 5
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX+75 and mouseY+125 <= pygame.mouse.get_pos()[1] <= mouseY+150:
                    return 6
            else:
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 25 <= pygame.mouse.get_pos()[
                    1] <= mouseY:
                    return 1
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 50 <= pygame.mouse.get_pos()[
                    1] <= mouseY - 25:
                    return 2
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 75 <= pygame.mouse.get_pos()[
                    1] <= mouseY - 50:
                    return 3
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 100 <= pygame.mouse.get_pos()[
                    1] <= mouseY - 75:
                    return 4
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 125 <= pygame.mouse.get_pos()[
                    1] <= mouseY - 100:
                    return 5
                if mouseX <= pygame.mouse.get_pos()[0] <= mouseX + 75 and mouseY - 150 <= pygame.mouse.get_pos()[
                    1] <= mouseY - 125:
                    return 6

        for underevent in pygame.event.get():
            if underevent.type == pygame.QUIT:
                sys.exit()
            elif underevent.type == pygame.KEYDOWN:
                if underevent.key == pygame.K_ESCAPE:
                    return


while 1:
    if pygame.mouse.get_pressed(3)[0]:
        while pygame.mouse.get_pressed(3)[0]:
            pygame.event.pump()
        dropdownMenu(screen, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 50, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
