import settings
from entity import *
from player import player

class camera:
    def __init__(self, _x, _y, _w, _h) -> None:
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h

        self.world = None

    def translate(self, obj: entity):
        obj.tranX = obj.x - self.x
        obj.tranY = obj.y - self.y

    def bindToPlayer(self, obj: player):
        #calculate center
        self.x = obj.x - settings.CENTERWIDTH
        self.y = obj.y - settings.CENTERHEIGHT

        #calculate To X Wall
        if self.x < 0:
            self.x = 0

        if self.x + self.w > self.world.worldSizeX:
            self.x = self.world.worldSizeX - self.w

        #calculate To Y Wall
        if self.y < 0:
            self.y = 0

        if self.y + self.h > self.world.worldSizeY:
            self.y = self.world.worldSizeY - self.h

    def decideDraw(self, obj: entity) -> bool:
        return (
            #x Achse
            obj.x <= self.x + self.w and obj.x + obj.w >= self.x and

            #y Achse
            obj.y <= self.y + self.h and obj.y + obj.h >= self.y
        )