import pygame
from settings import Settings

pygame.init()
gm_set = Settings()
screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
pygame.display.set_caption(gm_set.caption)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(gm_set.bg_color)
    pygame.display.flip()

pygame.quit()