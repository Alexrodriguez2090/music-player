import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.rect(screen, width=)

    pygame.display.flip()
#mixer.music.load("your-song.mp3")
#mixer.music.set_volume(0.6)
#mixer.music.play()