import pygame


def menuBox(window, x, y, width, height, text):
    pygame.draw.rect(window, (50, 50, 50), (x-5, y-5, width+10, height+10), 0, 5)
    if x - 5 <= pygame.mouse.get_pos()[0] <= x - 5 + width + 10 and y - 5 <= pygame.mouse.get_pos()[1] <= y - 5 + \
            height + 10:
        pygame.draw.rect(window, (128 + 30, 128 + 30, 128 + 30), (x, y, width, height), 0, 5)
    else:
        pygame.draw.rect(window, (128, 128, 128), (x, y, width, height), 0, 5)
    rectFont = pygame.font.SysFont("arial", 50)
    rectText = rectFont.render(text, False, (0, 0, 0))
    window.blit(rectText, ((x + (width/2))-(rectFont.size(text)[0]/2), (y + (height/2))-(rectFont.size(text)[1])/2))


def menuSlider(window, x, y, width, height, sliderPos, sbp, text):
    rectFont = pygame.font.SysFont("arial", 40)
    rectText = rectFont.render(text, False, (160, 160, 160))
    window.blit(rectText, (x + (width / 2), y - 60))
    pygame.draw.rect(window, (125, 125, 125), (x, y-(height/2), width + 6, height))
    pygame.draw.rect(window, (0, 0, 0), (x+3, (y-(height/2))+3, width, height - 6))
    if int(x-10+(width*sliderPos)) <= pygame.mouse.get_pos()[0] <= int(x-10+(width*sliderPos)) + 20 and y - height \
            <= pygame.mouse.get_pos()[1] <= y+height or sbp:
        pygame.draw.rect(window, (190, 190, 190), (int(x-10+(width*sliderPos)), y - height, 20, height * 2))
    else:
        pygame.draw.rect(window, (125, 125, 125), (int(x-10+(width*sliderPos)), y - height, 20, height * 2))
