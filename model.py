import random

import pygame


ball_in_sec=0
balls=[]
speedx=2
speedy=2
show_text=True
go=True



def ball_create():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    size = random.randint(3, 15)
    ball = {'color': color, 'cord': [x, y], 'size': size, 'speedx': random.randint(-20, 20),
            'speedy': random.randint(-20, 20)}
    balls.append(ball)


def ball_del():
    balls.clear()

def ball_change():
    global ball_in_sec
    ball_in_sec -= 1
    if ball_in_sec<0:
        ball_in_sec=0

def ball_to_wall():
    for ball in balls:
        if ball['cord'][0]>=500 and ball['cord'][1]>=500:
            if 1000-ball['cord'][0]>1000-ball['cord'][1]:
                ball['cord'][1] = 1000 - ball['size']
            else:
                ball['cord'][0] = 1000 - ball['size']
        if ball['cord'][0]<=500 and ball['cord'][1]<=500:
            if 0+ball['cord'][0]>0+ball['cord'][1]:
                ball['cord'][1] = 0 + ball['size']
            else:
                ball['cord'][0] = 0 + ball['size']
        if ball['cord'][0]<=500 and ball['cord'][1]>=500:
            if 0+ball['cord'][0]>1000-ball['cord'][1]:
                ball['cord'][1] = 1000 - ball['size']
            else:
                ball['cord'][0] = 0 + ball['size']
        if ball['cord'][0]>=500 and ball['cord'][1]<=500:
            if 1000-ball['cord'][0]>0+ball['cord'][1]:
                ball['cord'][1] = 0 + ball['size']
            else:
                ball['cord'][0] = 1000 - ball['size']
        print(ball['cord'])

def model():
    global speedy,speedx,ball_in_sec
    if not go:
        return
    for ball in balls:
        ball['cord'][0]+=ball['speedx']
        ball['cord'][1] += ball['speedy']
        if ball['cord'][0]>=1000-ball['size']:
            ball['cord'][0]=1000-ball['size']
            ball['speedx']=-ball['speedx']
        if ball['cord'][0]<=0+ball['size']:
            ball['cord'][0] =0+ball['size']
            ball['speedx']=-ball['speedx']
        if ball['cord'][1]>=1000-ball['size']:
            ball['cord'][1]=1000-ball['size']
            ball['speedy']=-ball['speedy']
        if ball['cord'][1]<=0+ball['size']:
            ball['cord'][1] =0+ball['size']
            ball['speedy']=-ball['speedy']
