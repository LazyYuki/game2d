import pygame, settings, math
from entity import *
from settings import staminaConsumption

class player(entity):
    jumpHeight = 300
    g = (2*jumpHeight)/(math.pow(settings.GRAVITY, 2))
    initJumpVelocity = math.sqrt(2*g*jumpHeight)
    onGround = False

    currentMaxHealth = settings.MINHEALTH
    health = currentMaxHealth

    currentMaxStamina = settings.MINSTAMINA
    stamina = currentMaxStamina

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

        if keys[pygame.K_SPACE] and self.onGround and self.stamina >= staminaConsumption.JUMP:
            self.stamina -= staminaConsumption.JUMP
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

        #stamina update
        if self.stamina >= self.currentMaxStamina:
            self.stamina = self.currentMaxStamina
        else:
            self.stamina += staminaConsumption.REGENERATIONRATE * dt

    def draw(self, screen):
        #draw character
        pygame.draw.rect(screen, settings.GREEN, (self.tranX, self.tranY, self.w, self.h))

        #draw Health and Stamina
        pygame.draw.rect(screen, settings.HEALTHCOLOR, (10, 10, self.health * settings.PIXELPERHEALTH, 10))
        pygame.draw.rect(screen, settings.STAMINACOLOR, (10, 30, self.stamina * settings.PIXELPERSTAMINA, 10))

        #draw health and stamina sidebars
        pygame.draw.rect(screen, settings.HESTSIDEBARCOLOR, (7, 7, 3, 16))
        pygame.draw.rect(screen, settings.HESTSIDEBARCOLOR, (self.currentMaxHealth * settings.PIXELPERHEALTH + 7, 7, 3, 16))

        pygame.draw.rect(screen, settings.HESTSIDEBARCOLOR, (7, 27, 3, 16))
        pygame.draw.rect(screen, settings.HESTSIDEBARCOLOR, (self.currentMaxStamina * settings.PIXELPERHEALTH + 7, 27, 3, 16))

