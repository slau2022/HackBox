import pygame as pg

class HackBox():
    def __init__(self):
        pg.init()
        width, height = 500, 500
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Hackbox")
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(60)

        self.screen.fill(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        pg.display.flip()


hb = HackBox()
while 1:
    hb.update()
