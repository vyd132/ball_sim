import pygame

import pygame,model

event_type=pygame.event.custom_type()


def event():
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_e:
            model.show_text= not model.show_text
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            model.ball_in_sec+=1
            pygame.time.set_timer(event_type, 0)
            pygame.time.set_timer(event_type, int(1000/model.ball_in_sec))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            model.ball_change()
            pygame.time.set_timer(event_type, 0)
            if model.ball_in_sec!=0:
                pygame.time.set_timer(event_type, int(1000 / model.ball_in_sec))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            model.ball_del()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            model.stop = not model.stop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            model.go = not model.go
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            model.wall=not model.wall
        if event.type==event_type:
            model.ball_create()