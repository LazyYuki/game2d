import pygame

class entity:
    def __init__(self,_x, _y, _z, _w, _h, _name) -> None:
        self.x = _x
        self.y = _y
        self.z = _z

        self.velX = 0
        self.velY = 0

        self.w = _w
        self.h = _h

        self.tranX = 0
        self.tranY = 0

        self.world = None

        self.name = _name

    def update(self, dt, keys, hitting):
        pass

    def draw(self, screen):
        pass