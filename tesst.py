import pygame

screen = pygame.display.set_mode((500, 500))

while 1:
    pygame.event.pump()
    if (150 < pygame.mouse.get_pos()[0] < 350) and (150 < pygame.mouse.get_pos()[1] < 350):
        pygame.draw.rect(screen, (0, 255, 0), (150, 150, 200, 200))
        print("YOOO")
    else:
        pygame.draw.rect(screen, (255, 0, 0), (150, 150, 200, 200))
    pygame.display.flip()
