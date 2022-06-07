import sys
from telnetlib import GA
import time
from tkinter import N
from turtle import Screen, screensize
from numpy import choose
import pygame
from config import *
from black_chess import Black_Chess
from white_chess import White_Chess
import pymunk.pygame_util

screen = pygame.display.set_mode((680,680))

all_sprites = pygame.sprite.Group()
white_sprites = pygame.sprite.Group()
white_one_sprite = pygame.sprite.Group()
black_sprites = pygame.sprite.Group()

ix = 40
iy = 50
dx_black = 0
dy_black = 0

dx_white = 1
dy_white = 1

dx_white1 = 0
dy_white1 = 0


number = 0

clock = pygame.time.Clock()
FPS = 60
for _ in range(8):
    w = White_Chess(screen, ix, iy, number)
    all_sprites.add(w)
    white_sprites.add(w)
    ix += 80
    number += 1
ix = 40
iy = 400

number = 0
for _ in range(8):
    w = Black_Chess(screen, ix, iy, number)
    all_sprites.add(w)
    black_sprites.add(w)
    ix += 80
    number += 1

num = 0
cnt = 0

def collide_2group():
    hits = pygame.sprite.groupcollide(white_one_sprite, black_sprites, False, False, pygame.sprite.collide_circle)
    if len(hits) > 0:
        bl_chess = list(hits.values())
        bl_chess = bl_chess[0][0]
        # print(list(white_sprites)[num])
        # print(white_sprites.values())
        if list(white_one_sprite)[num].rect.y > bl_chess.rect.y:
            dx_black1, dy_black1 = 0, -10
        elif list(white_one_sprite)[num].rect.y < bl_chess.rect.y:
            dx_black1, dy_black1 = 0, 10
        elif list(white_one_sprite)[num].rect.x > bl_chess.rect.x:
            dx_black1, dy_black1 = -10, 0
        elif list(white_one_sprite)[num].rect.x < bl_chess.rect.x:
            dx_black1, dy_black1 = 10, 0

        if list(white_one_sprite)[num].rect.x > bl_chess.rect.x and list(white_one_sprite)[num].rect.y > bl_chess.rect.y:
            dx_black1, dy_black1 = -10, -10
        elif list(white_one_sprite)[num].rect.x < bl_chess.rect.x and list(white_one_sprite)[num].rect.y < bl_chess.rect.y:
            dx_black1, dy_black1 = 10, 10
        elif list(white_one_sprite)[num].rect.x < bl_chess.rect.x and list(white_one_sprite)[num].rect.y > bl_chess.rect.y:
            dx_black1, dy_black1 = 10, -10
        elif list(white_one_sprite)[num].rect.x > bl_chess.rect.x and list(white_one_sprite)[num].rect.y < bl_chess.rect.y:
            dx_black1, dy_black1 = -10, 10
        bl_chess.update(dx_black1, dy_black1, num)

def collide_whiteGroup():
    global dx_white1
    global dy_white1
    global num 
    global cnt
    global white_sprites
    global white_one_sprite


    if len(white_one_sprite) == 0:
        white_one_sprite.add(list(white_sprites)[num])
        white_sprites.remove(list(white_sprites)[num])
        print(f"len1:{white_sprites}")
        cnt = num
        print(f'cnt:{cnt}')
    if cnt != num:
        white_sprites.add(list(white_one_sprite)[0])
        white_one_sprite.remove(list(white_one_sprite)[0])
        white_one_sprite.add(list(white_sprites)[0])
        white_sprites.remove(list(white_one_sprite)[0])
        cnt = num
        print(white_sprites)
        print("poi")
        



    hits_w = pygame.sprite.groupcollide(white_one_sprite, white_sprites, False, False, pygame.sprite.collide_circle)
    if len(hits_w) > 0:
        w_chess = list(hits_w.values())
        w_chess = w_chess[0][0]
        print("ooo")
        # print(white_sprites.values())
        if list(white_one_sprite)[0].rect.y > w_chess.rect.y:
            dx_white1, dy_white1 = 0, -10
        elif list(white_one_sprite)[0].rect.y < w_chess.rect.y:
            dx_white1, dy_white1 = 0, 10
        elif list(white_one_sprite)[0].rect.x > w_chess.rect.x:
            dx_white1, dy_white1 = -10, 0
        elif list(white_one_sprite)[0].rect.x < w_chess.rect.x:
            dx_white1, dy_white1 = 10, 0

        if list(white_one_sprite)[0].rect.x > w_chess.rect.x and list(white_one_sprite)[0].rect.y > w_chess.rect.y:
            dx_white1, dy_white1 = -10, -10
        elif list(white_one_sprite)[0].rect.x < w_chess.rect.x and list(white_one_sprite)[0].rect.y < w_chess.rect.y:
            dx_white1, dy_white1 = 10, 10
        elif list(white_one_sprite)[0].rect.x < w_chess.rect.x and list(white_one_sprite)[0].rect.y > w_chess.rect.y:
            dx_white1, dy_white1 = 10, -10
        elif list(white_one_sprite)[0].rect.x > w_chess.rect.x and list(white_one_sprite)[0].rect.y < w_chess.rect.y:
            dx_white1, dy_white1 = -10, 10
        w_chess.update1(dx_white1, dy_white1, num)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP5]:
        num += 1
        if num > 7:
            num = 0
        print(f"num:{num}, cnt:{cnt}")
        time.sleep(delay)
    if keys[pygame.K_KP8]:
        pass

    collide_2group()
    collide_whiteGroup()
    


    # for hit in hits:
    #     dx_black, dy_black = 0, 2
    #     print("h")

    screen.fill((255,255,255))
    white_one_sprite.update(dx_white, dy_white, num)
    black_sprites.update(dx_black, dy_black, num)
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.update()