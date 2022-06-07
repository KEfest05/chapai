import pygame
from config import *

class Black_Chess(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(black_chess_link)
        self.rect = self.image.get_rect()
        self.radius = 30
        self.screen = screen
        self.number = number
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy, i):
        self.rect.x += dx
        self.rect.y += dy

