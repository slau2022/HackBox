import pygame as pg


class HackBox():
    def __init__(self):
        pg.init()
        self.width, self.height = 600, 600
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Hackbox")
        self.font = pg.font.Font(None, 32)
        self.clock = pg.time.Clock()
        self.input_box = pg.Rect(0, 536, 600, 64)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.log = list()
        self.max_msg = 25;

    def loadingScreen(self):
        pygame.draw.rect(self.screen, 0, (50,50,100,100), 0)
        myfont = pg.font.SysFont("Comic Sans MS", 30)
        # apply it to text on a label
        label = myfont.render("Loading...", 1, (255,255,255))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (100, 100))
    
    def update(self):
        self.clock.tick(60)

        self.screen.fill(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = self.color_active if self.active else self.color_inactive
            if event.type == pg.KEYDOWN:
                if self.active:
                    if event.key == pg.K_RETURN:
                        self.log.append(self.text)
                        if len(self.log) > 25:
                            self.log.pop(0)
                        self.text = ''
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif len(self.text) < 40:
                        self.text += event.unicode
        # Render the current text.
        txt_surface = self.font.render(self.text[0:20], True, self.color)
        txt_surface2 = self.font.render(self.text[20:40], True, self.color)
        self.input_box.w = self.width / 2
        self.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        self.screen.blit(txt_surface2, (self.input_box.x + 5, self.input_box.y + 37))
        y = 0;
        for msg in self.log:
            msg_surface = self.font.render(msg[0:20], True, self.color)
            msg_surface2 = self.font.render(msg[20:40], True, self.color)
            self.screen.blit(msg_surface, (0, y))
            if len(msg) > 20 :
                y += 20
            self.screen.blit(msg_surface2, (0, y))
            y += 20
        pg.draw.rect(self.screen, self.color, self.input_box, 2)
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            pg.draw.rect(self.screen, (255, 0, 0), (pos[0] - 5, pos[1] - 5, 10, 10), 0)
        pg.display.flip()


hb = HackBox()
while 1:
    hb.update()
