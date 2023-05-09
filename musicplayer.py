import pygame
import subprocess
import tkinter
import tkinter.filedialog

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 18)

class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.enabled = True
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, "black")
        button_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

        if self.check_click():
            pygame.draw.rect(screen, "dark gray", button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, "gray", button_rect, 0, 5)

        pygame.draw.rect(screen, "black", button_rect, 2, 5)
        screen.blit(button_text, (self.x + 5, self.y + 5))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        #left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        if event.type == pygame.MOUSEBUTTONUP and button_rect.collidepoint(mouse_pos) and self.enabled:
            if self.text == "Load":
                return folder_prompt()
        else:
            return False

class Titlebar:
    def __init__(self, window_width):
        self.width = window_width
        self.close_button_x = 100
        self.close_button_y = self.width - 40
        self.all_buttons_width = 30
        self.all_buttons_height = 20
        self.draw()

    def draw(self):
        close_button_text = font.render("X", True, "black")
        close_button_rect = pygame.rect.Rect(self.close_button_y, self.close_button_x, self.all_buttons_width, self.all_buttons_height)

        pygame.draw.rect(screen, "gray", close_button_rect)
        screen.blit(close_button_text, (self.close_button_y, self.close_button_x))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        if event.type == pygame.MOUSEBUTTONUP and button_rect.collidepoint(mouse_pos) and self.enabled:
            return pygame.QUIT

def folder_prompt():
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askdirectory(parent=top)
    top.destroy()
    return file_name        

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True



while running:
    screen.fill("#0C134F")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    titlebar = Titlebar(SCREEN_WIDTH)

    load_button = Button(10, 10, 70, 20, "Load")

    pygame.display.flip()
#mixer.music.load("your-song.mp3")
#mixer.music.set_volume(0.6)
#mixer.music.play()