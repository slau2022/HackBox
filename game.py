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

        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            pg.draw.rect(self.screen, (255, 0, 0), (pos[0], pos[1], 10, 10), 0)
        pg.display.flip()


hb = HackBox()
while 1:
    hb.update()
