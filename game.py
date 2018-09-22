import pygame as pg

pg.init()
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
WIDTH = 1400
HEIGHT = 700
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, c, mx, my, text=''):
        self.input_box = pg.Rect(x, y, w, h)
        self.c = c
        self.mx = mx
        self.my = my
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.txt_surface2 = FONT.render(text, True, self.color)
        self.active = False
        self.log = list()
        self.max_msg = 1
        if c:
            self.max_msg = 27

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.input_box.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.log.append(self.text)
                    if len(self.log) > self.max_msg:
                        self.log.pop(0)
                    self.text = ''
                    return self.log[len(self.log) - 1]
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 60:
                    self.text += event.unicode
        return 0

    def update(self):
        # Render the current text.
        self.txt_surface = FONT.render(self.text[0:30], True, self.color)
        self.txt_surface2 = FONT.render(self.text[30:60], True, self.color)
        self.input_box.w = WIDTH / 2

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        screen.blit(self.txt_surface2, (self.input_box.x + 5, self.input_box.y + 37))
        #if self.c:
        y = self.my;
        for msg in self.log:
            msg_surface = FONT.render(msg[0:30], True, self.color)
            msg_surface2 = FONT.render(msg[30:60], True, self.color)
            screen.blit(msg_surface, (self.mx, y))
            if len(msg) > 20:
                y += 20
            screen.blit(msg_surface2, (self.mx, y))
            y += 20
        #else:
            #msg_surface = FONT.render(self.text[0:30], True, self.color)
            #msg_surface2 = FONT.render(self.text[30:60], True, self.color)
            #screen.blit(msg_surface, (WIDTH / 2, 300))
            #screen.blit(msg_surface2, (WIDTH / 2, 320))
        pg.draw.rect(screen, self.color, self.input_box, 2)


class HackBox():
    def __init__(self):
        self.state = 0
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Hackbox")
        self.clock = pg.time.Clock()
        self.chat_box = InputBox(0, HEIGHT - 64, WIDTH / 2, 64, True, 0, 0)
        self.question_input = InputBox(WIDTH / 2, HEIGHT - 64, WIDTH / 2, 64, False, WIDTH / 2, HEIGHT / 2)
        self.username_input = InputBox(0, HEIGHT - 64, WIDTH / 2, 64, False, WIDTH / 2, HEIGHT / 2)
        self.input_boxes = [self.chat_box, self.question_input]
        self.username = ''

    def introScreen(self):
        label = FONT.render("Please enter a username below", 1, (255, 255, 255))
        self.screen.blit(label, (0, 0))

    def loadingScreen(self):
        pg.draw.rect(self.screen, 0, (50, 50, 100, 100), 0)
        myfont = pg.font.SysFont("Comic Sans MS", 30)
        # apply it to text on a label
        label = myfont.render("Loading...", 1, (255, 255, 255))
        # put the label object on the screen at point x=100, y=100
        self.screen.blit(label, (WIDTH / 2, 0))

    def update(self):
        self.clock.tick(60)

        self.screen.fill(0)

        if self.state == 0:
            hb.introScreen()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                self.username = self.username_input.handle_event(event)
                if self.username != 0:
                    self.state += 1
            self.username_input.update()
            self.username_input.draw(self.screen)

        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()

            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                pg.draw.rect(self.screen, (255, 0, 0), (pos[0] - 5, pos[1] - 5, 10, 10), 0)

            for box in self.input_boxes:
                box.draw(self.screen)
        pg.display.flip()


hb = HackBox()
while 1:
    hb.update()
