import pygame, settings
from world import world
from player import player
from block import *
from entity import *
from camera import *

class game:
    def __init__(self, _screen) -> None:
        self.screen = _screen

        self.camera = camera(0, 0, 100, 100)

        self.entityList = []
        self.blockList = []

        self.loadWorld(world())

    def loadWorld(self, w: world):
        self.entityList = w.loadEntity()
        self.blockList = w.loadBlock()

        self.camera = w.camera
        self.player = w.player

    def checkCollision(self, obj1: entity, obj2: entity):
        return (
            #x Achse
            obj1.x <= obj2.x + obj2.w and obj1.x + obj1.w >= obj2.x and

            #y Achse
            obj1.y <= obj2.y + obj2.h and obj1.y + obj1.h >= obj2.y
        )

    def update(self, dt, keys):
        e: entity
        for e in self.entityList:
            collisionList = {}

            j: entity
            for j in self.entityList:
                if e == j: continue

                if self.checkCollision(e, j):

                    if j.name in collisionList:
                        collisionList[j.name].append(j)
                    else:
                        collisionList[j.name] = [j]

            b: block
            for b in self.blockList:
                if self.checkCollision(e, b):
                    if b.name in collisionList:
                        collisionList[b.name].append(b)
                    else:
                        collisionList[b.name] = [b]

            e.update(dt, keys, collisionList)

    def draw(self):
        #bind camera To player
        self.camera.bindToPlayer(self.player)

        b: block
        for b in self.blockList:
            if self.camera.decideDraw(b):
                self.camera.translate(b)
                b.draw(self.screen)

        e: entity
        for e in self.entityList:
            
            # TODO: sort by z achse

            if self.camera.decideDraw(e):
                self.camera.translate(e)
                e.draw(self.screen)