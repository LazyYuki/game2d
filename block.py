import pygame

class block:
    def __init__(self,_x, _y, _z, _w, _h, _name, _color) -> None:
        self.x = _x
        self.y = _y
        self.z = _z
        
        self.w = _w
        self.h = _h

        self.tranX = 0
        self.tranY = 0

        self.name = _name

        self.color = _color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.tranX, self.tranY, self.w, self.h))