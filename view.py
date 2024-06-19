import pygame,model
pygame.init()
screen=pygame.display.set_mode([1000,1000])
font=pygame.font.SysFont('arial',30)
text_E=font.render('Нажмите E для показа/скрытия подсказок',True,[255,0,0],[255,255,255])
text_active=font.render('Режимы: 1 - стоп, 2 - свободный полет, 3 - прилипание к стене',True,[255,0,0],[255,255,255])

def view():
    global screen
    screen.fill([0, 0, 0])
    text_gen = font.render('Шариков в секунду ' + str(model.ball_in_sec) + ': ВВЕРХ: увел., ВНИЗ: уменьш.', True,
                           [255, 0, 0], [255, 255, 255])
    text_ball_col = font.render('Шариков на экране ' + str(len(model.balls)) + ': DEL: удалить все шарики', True,
                           [255, 0, 0], [255, 255, 255])
    for ball in model.balls:
        pygame.draw.circle(screen,ball['color'],ball['cord'],ball['size'])
    if model.show_text:
        screen.blit(text_E,[0,50])
        screen.blit(text_gen, [0, 80])
        screen.blit(text_ball_col, [0, 110])
        screen.blit(text_active, [0, 140])

    pygame.display.flip()
