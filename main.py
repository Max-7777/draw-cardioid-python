from lib2to3.pgen2 import pgen
import pygame as pg
import math

class Circle:
    def __init__(self, main, radius, points):
        self.main = main
        self.radius = radius
        self.points = points
        self.translate = self.main.screen.get_width() // 2, self.main.screen.get_height() // 2
    
    def draw(self, mult):
        for i in range(self.points):
            angle = ((math.pi * 2) / self.points) * i
            x1 = self.radius * math.cos(angle) + self.translate[0]
            y1 = self.radius * math.sin(angle) + self.translate[1]

            x2 = self.radius * math.cos(angle*mult) + self.translate[0]
            y2 = self.radius * math.sin(angle*mult) + self.translate[1]

            pg.draw.aaline(self.main.screen, 'blue', (x1,y1), (x2,y2))


class Main:
    def __init__(self):
        self.screen = pg.display.set_mode([500,500])
        self.clock = pg.time.Clock()
        self.circle = Circle(self, 200, 40)

    def draw(self):
        self.screen.fill("black")

        mult = 2

        #mult = (math.sin(pg.time.get_ticks() * 0.0005)*3) + 4

        self.circle.draw(mult)

        pg.display.set_caption("MULT: {} FPS: {}".format(str(mult), self.clock.get_fps()))
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()