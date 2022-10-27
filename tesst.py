import pygame

screen = pygame.display.set_mode((500, 500))

while 1:
    if (150 < pygame.mouse.get_pos()[0] and 350 > pygame.mouse.get_pos()[0]) and (150 < pygame.mouse.get_pos()[1] and 350 > pygame.mouse.get_pos()[1]):
        pygame.draw.rect(screen, (0, 255, 0), (150, 150, 200, 200))
        print("YOOO")
    else:
        pygame.draw.rect(screen, (255, 0, 0), (150, 150, 200, 200))
    pygame.display.flip()
