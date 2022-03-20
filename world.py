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

        #test level
        p1 = block(100, self.worldSizeY - 300, 0, 200, 30, "ground", settings.WHITE)
        p2 = block(300, self.worldSizeY - 200, 0, 100, 30, "ground", settings.WHITE)

        self.entityList.append(p)

        self.blockList = [ground, p1, p2]

    def loadWorldFromFile():
        #TODO load from file

        return world()

    def loadEntity(self) -> list:
        return self.entityList

    def loadBlock(self) -> list:
        return self.blockList