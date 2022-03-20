import pygame, settings
from entity import *

class player(entity):
    def update(self, dt, keys, hitting):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, settings.GREEN, (self.tranX, self.tranY, self.h, self.w))