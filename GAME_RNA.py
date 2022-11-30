import numpy as n
import pygame as pg
#from Nucleozid import *
import pygame.freetype
#from Iscander import *
import thorpy
import random
import sys
def RNA_GAME():
    SCREEN_SIZE = (1000, 700)
    pg.init()
    name = 'Игрок 1'
    screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BROWN = (210, 105, 30)
    WHITE = (255, 255, 255)
    ORANGE = (255, 165, 0)

    FPS = 30
    size = 18
    org = 80
    c0 = 140
    c1 = org
    PO4 = 5
    FONT = pg.freetype.Font(None, size)
    seq=""
    number=random.randint(30,45)
    for i in range(number):
        seq+=random.choice('ACGT')

    '''Часть Полины'''


    class Animation:
        def __init__(self, screenSize):
            self.RED = (255, 0, 0)
            self.GREEN = (0, 255, 0)
            self.YELLOW = (255, 255, 0)
            self.MAGENTA = (255, 0, 255)
            self.screenSize = screenSize
            self.rectsize = 18
            self.x = random.randint(0, screenSize[0] - 18)
            self.y = random.randint(0, screenSize[1] - 18)
            self.xSpeed = random.randint(-100, 100)
            self.ySpeed = random.randint(-100, 100)

        def move(self, sec):
            self.x += sec * self.xSpeed
            self.y += sec * self.ySpeed
            if self.x + self.rectsize > self.screenSize[0]:
                self.xSpeed = -self.xSpeed
                self.x = self.screenSize[0] - self.rectsize
            if self.x < 0:
                self.xSpeed = -self.xSpeed
                self.x = 0
            if self.y + self.rectsize > self.screenSize[1]:
                self.ySpeed = -self.ySpeed
                self.y = self.screenSize[1] - self.rectsize
            if self.y < 0:
                self.ySpeed = -self.ySpeed
                self.y = 0

        def getXCoordinates(self):
            return self.x

        def getYCoordinates(self):
            return self.y

        def changeSpeed(self, speed):
            self.xSpeed = 0
            self.ySpeed = 0

        def setCoordinates(self, coord):
            self.x = coord[0]
            self.y = coord[1]

        def drawA(self, screen):
            pg.draw.rect(screen, self.RED, (self.x, self.y, self.rectsize, self.rectsize))
            pg.draw.polygon(screen, self.RED,
                            [(self.x, self.y), (self.x + 18, self.y), (self.x + 18 // 2, self.y - 18 // 2)])
            pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "A", (0, 0, 0))

        def drawT(self, screen):
            pg.draw.rect(screen, self.GREEN, (self.x, self.y, self.rectsize, self.rectsize))
            pg.draw.polygon(screen, self.GREEN, [(self.x, self.y), (self.x + 18 // 2, self.y), (self.x, self.y - 18 // 2)])
            pg.draw.polygon(screen, self.GREEN,
                            [(self.x + 18, self.y), (self.x + 18 // 2, self.y), (self.x + 18, self.y - 18 // 2)])
            pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "T", (0, 0, 0))

        def drawC(self, screen):
            pg.draw.rect(screen, self.MAGENTA, (self.x, self.y, self.rectsize, self.rectsize))
            pg.draw.rect(screen, self.MAGENTA, (self.x + 18 // 3, self.y - 18 // 2, 18 // 3, 18 // 2))
            pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "C", (0, 0, 0))

        def drawG(self, screen):
            pg.draw.rect(screen, self.YELLOW, (self.x, self.y, self.rectsize, self.rectsize))
            pg.draw.rect(screen, self.YELLOW, (self.x, self.y - 18 // 2, 18 // 3, 18 // 2))
            pg.draw.rect(screen, self.YELLOW, (self.x + 2 * 18 // 3, self.y - 18 // 2, 18 // 3, 18 // 2))
            pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "G", (0, 0, 0))

    '''Часть Артема
       Задает параметры построения РНК при нажатии клавишь
       фунцкия Ad-строит аденин
               Cyt строит цитозин
               Gua-строит гуанин
               Ura-строит урацил'''
    def Ad(a,y,h):
        pg.draw.polygon(screen, RED,[(a,y),(a+h,y),(a+h,y+h),(a+int(h/2),y+int(h*1.5)),(a,y+h)])
        pg.draw.line(screen, CYAN,(a+h,y+int(h/2)),(a+int(h*length),y+int(h/2)),5)
        FONT.render_to(screen, (a+int(0.2*h),y+int(0.2*h)), "A", (255, 255, 255))
        pg.display.update()

    def Cyt(a,y,h):
        pg.draw.polygon(screen, MAGENTA,[(a,y),(a+h,y),(a+h,y+h),(a+int(0.7*h),y+h),(a+int(0.7*h),y+int(1.5*h)),
                                         (a+int(0.3*h),y+int(1.3*h)),(a+int(0.3*h),y+h), (a,y+h)])
        pg.draw.line(screen, CYAN,(a+h,y+int(0.5*h)),(a+int(h*length),y+int(h/2)),5)
        FONT.render_to(screen, (a+int(0.2*h),y+int(0.2*h)), "C", (255, 255, 255))
        pg.display.update()

    def Gua( a, y,h):
        pg.draw.polygon(screen, YELLOW, [(a, y), (a + h, y), (a + h, y + int(1.5*h)), (a + int(0.7*h), y + int(1.5*h)),
                                         (a+int(0.7*h), y + h),(a+int(0.3*h),y+h),(a+int(0.3*h),y+int(1.5*h)),(a,y+int(1.5*h))])
        pg.draw.line(screen, CYAN, (a + h, y + int(0.5 * h)), (a + int(h*length), y + int(h / 2)), 5)
        FONT.render_to(screen, (a+int(0.2*h),y+int(0.2*h)), "G", (255, 255, 255))
        pg.display.update()
    def Ura(a, y,h):
        pg.draw.polygon(screen, GREEN, [(a, y), (a + h, y), (a + h, y + int(1.5*h)), (a + int(h / 2), y + h),
                                        (a, y + int(1.5*h)),(a+int(0.3*h),y+h)])
        pg.draw.line(screen, CYAN, (a + h, y + int(0.5 * h)), (a + int(h*length), y + int(h / 2)), 5)
        FONT.render_to(screen, (a+int(0.2*h),y+int(0.2*h)), "U", (255, 255, 255))
        pygame.display.update()
    def start_execution():
        """Обработчик события нажатия на кнопку Start.
        Запускает циклическое исполнение функции execution.
        """
        global perform_execution
        perform_execution = True

    '''Часть Искандера
        отвечает за построение ДНК и 
        РНК-полимиразы'''
    def a_draw(coord, size):
        pg.draw.rect(screen, RED, (coord[0], coord[1], size, size))
        pg.draw.polygon(screen, RED, [(coord[0], coord[1]),
                                      (coord[0] + size, coord[1]), (coord[0] + size // 2, coord[1] - size // 2)])
        FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "A", BLACK)


    def t_draw(coord, size):
        pg.draw.rect(screen, GREEN, (coord[0], coord[1], size, size))
        pg.draw.polygon(screen, GREEN, [(coord[0], coord[1]),
                                        (coord[0] + size // 2, coord[1]), (coord[0], coord[1] - size // 2)])
        pg.draw.polygon(screen, GREEN, [(coord[0] + size, coord[1]),
                                        (coord[0] + size // 2, coord[1]), (coord[0] + size, coord[1] - size // 2)])
        FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "T", BLACK)


    def c_draw(coord, size):
        pg.draw.rect(screen, MAGENTA, (coord[0], coord[1], size, size))
        pg.draw.rect(screen, MAGENTA, (coord[0] + size // 3, coord[1] - size // 2, size // 3, size // 2))
        FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "C", BLACK)


    def g_draw(coord, size):
        pg.draw.rect(screen, YELLOW, (coord[0], coord[1], size, size))
        pg.draw.rect(screen, YELLOW, (coord[0], coord[1] - size // 2, size // 3, size // 2))
        pg.draw.rect(screen, YELLOW, (coord[0] + 2 * size // 3, coord[1] - size // 2, size // 3, size // 2))
        FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "G", BLACK)


    def DNA(coord):
        pg.draw.arc(screen, CYAN, (org - 80, SCREEN_SIZE[1] - 178, 70, 50), n.pi / 2, n.pi * 3 / 2, 5)
        a = pg.Surface((SCREEN_SIZE))
        a.fill(ORANGE)
        pg.draw.ellipse(a, BLACK, (0, 0, 100, 70))
        a.set_colorkey(ORANGE)
        a = pg.transform.rotate(a, 90)
        screen.blit(a, (c1 - (size + PO4), -420))

        pg.draw.rect(screen, YELLOW, (org // 5, SCREEN_SIZE[1] - 170, size, size))
        pg.draw.rect(screen, MAGENTA, (org // 5, SCREEN_SIZE[1] - 150, size, size))
        pg.draw.rect(screen, YELLOW, (org, SCREEN_SIZE[1] - 200, size * 3, size))
        pg.draw.rect(screen, MAGENTA, (org, SCREEN_SIZE[1] - 150, size * 3, size))
        pg.draw.line(screen, CYAN, [org // 2, SCREEN_SIZE[1] - 200 + size],
                     [c0 + len(seq) * (size + PO4), SCREEN_SIZE[1] - 200 + size], 5)
        pg.draw.line(screen, CYAN, [org // 2, SCREEN_SIZE[1] - 150 + size],
                     [c0 + len(seq) * (size + PO4), SCREEN_SIZE[1] - 150 + size], 5)
        # topoasa
        a = pg.Surface((SCREEN_SIZE))
        pg.draw.ellipse(a, BROWN, (0, 0, 90, 60))
        FONT.render_to(a, (6, 10), "topoiso", WHITE)
        FONT.render_to(a, (6, 28), "merase", WHITE)
        a.set_colorkey(BLACK)
        a = pg.transform.rotate(a, 90)
        screen.blit(a, (org // 4, -425))
        # seq
        for i in range(len(seq)):
            if seq[i] == 'A':
                a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
            if seq[i] == 'G':
                g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
            if seq[i] == 'T':
                t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
            if seq[i] == 'C':
                c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)


    def Pasa(coord):
        a = pg.Surface((SCREEN_SIZE))
        pg.draw.ellipse(a, ORANGE, (0, 0, 100, 70))
        FONT.render_to(a, (6, 10), "RNA poly", WHITE)
        FONT.render_to(a, (6, 28), "merase", WHITE)
        a.set_colorkey(BLACK)
        a = pg.transform.rotate(a, 90)
        screen.blit(a, (c1, -420))

    '''Часть Артема 
       в этой части уже идет взаимодействие с клавиатурой
       и само построение РНК
       при нажатии клавиши 'G,U,C,A' 
       появляются соответственно гуанин,
       урацил, цитозин и Аденин'''
    def Menu():
        '''Создает окно запуска'''
        button_play = thorpy.make_button("Play",start_execution)
        timer = thorpy.OneLineText("Seconds passed")
        box = thorpy.Box(elements=[
            button_play,
            timer])
        my_reaction = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                      reac_func=start_execution)
        menu = thorpy.Menu(box)
        for element in menu.get_population():
            element.surface = screen

        box.set_topleft((0, 0))
        box.blit()
        box.update()
        return menu,box,timer
    pg.draw.line(screen,WHITE,(0,int(SCREEN_SIZE[1]/2)),(SCREEN_SIZE[0],int(SCREEN_SIZE[1]/2)))
    pg.display.update()
    x=142
    z=460
    h=14.9
    length=1.55
    count=0
    finished = False
    str1=''
    perform_execution = False
    rectList = []
    screenSize1=(SCREEN_SIZE[0],int(SCREEN_SIZE[1]/2))
    rectList = []
    for i in range(4):
        rect = Animation(screenSize1)
        rectList.append(rect)
    rectList1 = []
    for i in range(4):
        rect = Animation(screenSize1)
        rectList1.append(rect)
    rectList2 = []
    for i in range(4):
        rect = Animation(screenSize1)
        rectList2.append(rect)
    rectList3 = []

    for i in range(4):
        rect = Animation(screenSize1)
        rectList3.append(rect)

    for i in range(len(seq)):
        if seq[i] == 'A':
            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'G':
            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'T':
            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'C':
            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)

    while not finished:
        menu, box, timer = Menu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finished = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                menu.react(event)
                if perform_execution:
                    for i in range(len(seq)):
                        if seq[i] == 'A':
                            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                        if seq[i] == 'G':
                            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                        if seq[i] == 'T':
                            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                        if seq[i] == 'C':
                            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    Ura(x, z, h)
                    x += int(h * length)
                    str1 += 'A'
                    c1 += (size + PO4)
                    count += 1
                    DNA(org)
                    Pasa(c0)
                elif event.key == pg.K_a:
                    Ad(x, z, h)
                    x += int(h * length)
                    str1 += 'T'
                    c1 += (size + PO4)
                    count += 1
                    DNA(org)
                    Pasa(c0)
                elif event.key == pg.K_c:
                    Cyt(x, z, h)
                    x += int(h * length)
                    str1 += 'G'
                    c1 += (size + PO4)
                    count += 1
                    DNA(org)
                    Pasa(c0)
                elif event.key == pg.K_g:
                    Gua(x, z, h)
                    x += int(h * length)
                    str1 += 'C'
                    c1 += (size + PO4)
                    count += 1
                    DNA(org)
                    Pasa(c0)
        sec = clock.tick() / 1000.
        for rect in rectList:
            rect.move(sec)
        for rect in rectList1:
            rect.move(sec)
        for rect in rectList2:
            rect.move(sec)
        for rect in rectList3:
            rect.move(sec)

        pg.draw.rect(screen,(0,0,0), pygame.Rect((0, 0), screenSize1))

        for rect in rectList:
            rect.drawA(screen)
        for rect in rectList1:
            rect.drawT(screen)
        for rect in rectList2:
            rect.drawC(screen)
        for rect in rectList3:
            rect.drawG(screen)
        if x > 1000:
            pg.draw.rect(screen, BLACK, (0, z, SCREEN_SIZE[0], 2 * h))
            x=110
        if c1 >= SCREEN_SIZE[0] - 100:
            org -= SCREEN_SIZE[0] * 2 // 3
            c0 -= SCREEN_SIZE[0] * 2 // 3
            c1 -= SCREEN_SIZE[0] * 2 // 3
            pg.draw.rect(screen, BLACK, (0, SCREEN_SIZE[1] - 220, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        if count == len(seq):
            finished = True
        clock.tick(FPS)
    pg.quit()
    pg.init()
    FPS = 30
    popal=0
    screen = pygame.display.set_mode((1000, 800))
    for i in range(len(seq)):
        if seq[i]==str1[i]:
            popal+=1
    procent=int(popal/len(seq)*100)

    FONT=pygame.freetype.Font(None, 20)
    FONT.render_to(screen, (50, 50), "Истинная строка " + seq, ORANGE)
    FONT.render_to(screen, (50, 150), "Ваша  строка " + str1, ORANGE)
    FONT1=pygame.freetype.Font(None, 20)

    FONT1.render_to(screen, (50, 250), "Вы биотехнолог на " + str(procent)+'%', ORANGE)
    FONT1.render_to(screen, (50, 350), "Вы превзошли " + str(state)+"% пользователей", ORANGE)
    pg.display.update()
    clock = pygame.time.Clock()
    clock.tick(1)

    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finished = True

    pg.quit()
    try:
        file = open('table.txt', 'r')
    except:
        file = open('table.txt', 'w')
        file.close()
        file = open('table.txt', 'r')

    '''запись в файл'''
    s = file.read()
    file.close()
    out = open('table.txt', 'w', encoding= 'utf8')
    out.write(s+'\n'+ name + " биотехнолог на " + str(procent)+" %")
    out.close()
