import os
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    print(fullname)
    if not os.path.isfile(fullname):
        print('problema')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def intro():
    font = pygame.font.Font(None, 35)
    text = font.render('Об игре', 1, 'white')
    text_x = 210
    text_y = 300
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'white', (text_x - 10, text_y - 10, text_w + 20,
                                       text_h + 20), 5)

    text = font.render('Играть', 1, 'white')
    text_x = 225
    text_y = 370
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, 'white', (text_x - 10, text_y - 10, text_w + 20,
                                       text_h + 20), 5)


running = True
while running:
    intro()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if 210 <= x <= 419 and 290 <= y <= 356:
                pygame.draw.rect(screen, (105, 105, 105),
                                 (200, 290, 115, 45), 5)
                pygame.display.flip()
            if 225 <= x <= 404 and 360 <= y <= 426:
                pygame.draw.rect(screen, (105, 105, 105),
                                 (215, 360, 100, 45), 5)
                pygame.display.flip()
pygame.quit()