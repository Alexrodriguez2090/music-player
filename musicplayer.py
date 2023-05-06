import pygame

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
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True



while running:
    screen.fill("blue")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    load_button = Button(10, 10, 70, 20,"Load")

    pygame.display.flip()
#mixer.music.load("your-song.mp3")
#mixer.music.set_volume(0.6)
#mixer.music.play()