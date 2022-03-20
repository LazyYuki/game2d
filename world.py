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

        self.player = None

        self.test()

    def test(self):
        self.worldSizeX = 1300
        self.worldSizeY = 1600

        p = player(0, self.worldSizeY-50, 0, 30, 50, "player")
        p.world = self

        ground = block(0, self.worldSizeY-20, 0, self.worldSizeX, 20, "ground", settings.WHITE)

        #test level
        p1 = block(100, self.worldSizeY - 300, 0, 200, 30, "ground", settings.WHITE)
        p2 = block(300, self.worldSizeY - 200, 0, 100, 30, "ground", settings.WHITE)
        p3 = block(500, self.worldSizeY - 400, 0, 100, 30, "ground", settings.WHITE)

        self.entityList.append(p)

        self.blockList = [ground, p1, p2, p3]

        self.camera = camera(0, self.worldSizeY - settings.HEIGHT, settings.WIDTH, settings.HEIGHT)
        self.camera.world = self

        self.player = p

    def loadWorldFromFile():
        #TODO load from file

        return world()

    def loadEntity(self) -> list:
        return self.entityList

    def loadBlock(self) -> list:
        return self.blockList