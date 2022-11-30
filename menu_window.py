import pygame
import time
from maze import founding
from GAME_RNA import RNA_GAME
from survave import survave_game
import interview
pygame.init()
display = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_clr = (153, 153, 255)
        self.active_clr = (102, 102, 255)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and  y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))

            if click[0] == 1:
                if action is not None:
                    action()
        else:
            pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))
        print_text(message, x + 10, y + 10)


def quiz():
    Text_q, Text_dict = interview.convert_question()
    diagnoz = interview.open_window(Text_q, Text_dict, 'Пациент')
    return diagnoz
def show_menu():
    menu_bckgr = pygame.image.load('Menu.jpg')
    show = True

    patient_btn = Button(200, 50, (153, 153, 255), (102, 102, 255))
    doctor_btn = Button(470, 50, (153, 153, 255), (102, 102, 255))
    survave_btn = Button(300, 50, (153, 153, 255), (102, 102, 255))
    interview_btn = Button(330, 50, (153, 153, 255), (102, 102, 255))

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(menu_bckgr, (0, 0))
        patient_btn.draw(200, 233, 'Играть за пациента', founding)
        survave_btn.draw(200, 130, 'Дезинфекция', survave_game)
        doctor_btn.draw(200, 350, 'Играть за врача-исследователя', RNA_GAME)
        interview_btn.draw(200, 467, 'Пройти обследование',quiz)


        pygame.display.update()
        clock.tick(120)
def print_text (message, x, y, font_color = (153, 0, 76), font_type = 'arial.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x,y))

show_menu()
