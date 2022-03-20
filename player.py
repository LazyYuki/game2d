import pygame, settings, math
from entity import *

class player(entity):
    jumpHeight = 300
    g = (2*jumpHeight)/(math.pow(settings.GRAVITY, 2))
    initJumpVelocity = math.sqrt(2*g*jumpHeight)
    onGround = False

    def loadCharacter(self, dirPath):
        #TODO load all
        pass

    def processKeys(self, keys, hitting):
        if keys[pygame.K_d]:
            self.velX = 20
        elif keys[pygame.K_a]:
            self.velX = -20

        if "ground" in hitting:
            ground = hitting["ground"][0]

            #check bottom
            if self.y <= ground.y + ground.h and self.y >= ground.y:
                self.y = ground.y + ground.h
                self.velY = 1

            #check top
            elif self.y + self.h <= ground.y + ground.h:
                self.y = ground.y - self.h
                self.velY = 0
                self.onGround = True
        else: 
            self.onGround = False

        if keys[pygame.K_SPACE] and self.onGround:
            self.velY = -self.initJumpVelocity
            self.onGround = False

    def update(self, dt, keys, hitting):
        self.processKeys(keys, hitting)

        #x pos
        self.x += self.velX * dt
        self.velX *= 0.95

        if self.velX < 1 and self.velX > -1:
            self.velX = 0
        else:
            #TODO: PlayerAnimation

            pass

        if self.x <= 0:
            self.x = 0

        if self.x + self.w >= self.world.worldSizeX:
            self.x = self.world.worldSizeX - self.w

        #y pos
        if not self.onGround:
            self.y += self.velY * dt
            self.velY += settings.GRAVITY * dt


    def draw(self, screen):
        pygame.draw.rect(screen, settings.GREEN, (self.tranX, self.tranY, self.w, self.h))