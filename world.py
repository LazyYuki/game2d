import pygame, settings
from player import player
from block import *
from camera import *

class world:
    def __init__(self) -> None:
        self.entityList = []
        self.blockList = []

        self.worldSizeX = 0
        self.worldSizeY = 0

        self.camera = None

        self.test()

    def test(self):
        self.worldSizeX = 1600
        self.worldSizeY = 1600

        self.camera = camera(0, self.worldSizeY - settings.HEIGHT, settings.WIDTH, settings.HEIGHT)

        p = player(0, self.worldSizeY-30, 0, 10, 10, "player")

        ground = block(0, self.worldSizeY-20, 0, self.worldSizeX, 20, "ground", settings.WHITE)

        self.entityList.append(p)
        self.blockList.append(ground)

    def loadWorldFromFile():
        #TODO load from file

        return world()

    def loadEntity(self) -> list:
        return self.entityList

    def loadBlock(self) -> list:
        return self.blockList