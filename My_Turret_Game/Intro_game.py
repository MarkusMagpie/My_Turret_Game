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