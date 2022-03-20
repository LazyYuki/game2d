from tkinter import Y
from entity import *

class camera:
    def __init__(self, _x, _y, _w, _h) -> None:
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h

    def translate(self, obj: entity):
        obj.tranX = obj.x - self.x
        obj.tranY = obj.y - self.y


    def decideDraw(self, obj: entity) -> bool:
        print(obj.name)
        print(obj.x, obj.y, obj.w, obj.h)
        print(self.x, self.y, self.w, self.h)

        print(obj.x <= self.x + self.w)

        print(obj.x + obj.w >= self.x)

        print(obj.y <= self.y + self.h)

        print(obj.y + obj.h >= self.y)
        print("\n")

        return (
            #x Achse
            obj.x <= self.x + self.w and obj.x + obj.w >= self.x and

            #y Achse
            obj.y <= self.y + self.h and obj.y + obj.h >= self.y
        )