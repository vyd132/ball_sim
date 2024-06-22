import random

import pygame


ball_in_sec=0
balls=[]
speedx=19
speedy=19
show_text=True
go=True
wall=False
stop=False

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

def move_to_wall(cord,speed,side,object):
    object['cord'][cord] += speed
    if side=='left':
        if object['cord'][cord] <= 0 + object['size']:
            object['cord'][cord] = 0 + object['size']
    if side == 'right':
        if object['cord'][cord] >= 1000 - object['size']:
            object['cord'][cord] = 1000 - object['size']


def ball_to_wall():
    for ball in balls:
        if ball['cord'][0]>=500 and ball['cord'][1]>=500:
            if 1000-ball['cord'][0]>1000-ball['cord'][1]:
                move_to_wall(1,speedy,'right',ball)
            else:
                move_to_wall(0,speedx,'right',ball)
        if ball['cord'][0]<=500 and ball['cord'][1]<=500:
            if 0+ball['cord'][0]>0+ball['cord'][1]:
                move_to_wall(1,-speedy,'left',ball)
            else:
                move_to_wall(0,-speedx,'left',ball)
        if ball['cord'][0]<=500 and ball['cord'][1]>=500:
            if 0+ball['cord'][0]>1000-ball['cord'][1]:
                move_to_wall(1,speedy,'right',ball)
            else:
                move_to_wall(0,-speedx,'left',ball)
        if ball['cord'][0]>=500 and ball['cord'][1]<=500:
            if 1000-ball['cord'][0]>0+ball['cord'][1]:
                move_to_wall(1,-speedy,'left',ball)
            else:
                move_to_wall(0,speedx,'right',ball)


def model():
    global speedy,speedx,ball_in_sec
    if stop:
        return
    if wall:
        ball_to_wall()
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
