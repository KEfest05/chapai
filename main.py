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
dx_black = 5
dy_black = 5

dx_white = 1
dy_white = 1

dx_white1 = 0
dy_white1 = 0

# color = "white"

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
cl_cnt = 1

def collide(color):
    a_sprites = pygame.sprite.Group()
    a_sprites = all_sprites.copy()
    for chess in all_sprites:
            a_sprites.remove(chess)
            hit = pygame.sprite.spritecollide(chess, a_sprites, False, pygame.sprite.collide_circle)
            if len(hit) > 0:
                hit_c = hit[0]
                print(f"hit_c:{hit_c}")
                if hit_c.rect.y > chess.rect.y:
                    dx_white1, dy_white1 = 0, 10
                if hit_c.rect.y < chess.rect.y:
                    dx_white1, dy_white1 = 0, -10
                if hit_c.rect.x > chess.rect.x:
                    dx_white1, dy_white1 = 10, 0
                if hit_c.rect.x < chess.rect.x:
                    dx_white1, dy_white1 = -10, 0

                if hit_c.rect.x > chess.rect.x and hit_c.rect.y > chess.rect.y:
                    dx_white1, dy_white1 = 10, 10
                if hit_c.rect.x < chess.rect.x and hit_c.rect.y < chess.rect.y:
                    dx_white1, dy_white1 = -10, -10
                if hit_c.rect.x < chess.rect.x and hit_c.rect.y > chess.rect.y:
                    dx_white1, dy_white1 = -10, 10
                if hit_c.rect.x > chess.rect.x and hit_c.rect.y < chess.rect.y:
                    dx_white1, dy_white1 = 10, -10

                if color == "white":
                    hit_c.update1(dx_white1, dy_white1, num)
                if color == "black":
                    chess.update1(-dx_white1, -dy_white1, num)
                # a_sprites.add(chess)

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
        cl_cnt = -cl_cnt 
        time.sleep(delay)

    if cl_cnt == 1:
        color = "white"
    if cl_cnt == -1:
        color = "black"

    # collide_2group()
    # collide_whiteGroup()
    collide(color)

    screen.fill((255,255,255))
    all_sprites.update(dx_black, dy_black, num, color)
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.update()