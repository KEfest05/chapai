import pygame
from config import *

class Black_Chess(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(black_chess_link)
        self.rect = self.image.get_rect()
        self.radius = 28
        self.screen = screen
        self.number = number
        self.rect.x = x
        self.rect.y = y
        self.color = "black"

    def update(self, dx, dy, i, color):
        keys = pygame.key.get_pressed()
        if color == "black":
            if keys[pygame.K_RIGHT] and i == self.number:
                self.rect.x += dx
            if keys[pygame.K_DOWN] and i == self.number:
                self.rect.y += dy
            if keys[pygame.K_LEFT] and i == self.number:
                self.rect.x -= dx
            if keys[pygame.K_UP] and i == self.number:
                self.rect.y -= dy

    def update1(self, dx, dy, i):
        self.rect.x += dx
        self.rect.y += dy

