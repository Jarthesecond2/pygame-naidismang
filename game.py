import pygame
from settings import Settings
from player import Player
from bubble import Bubble
import game_functions as gf

def run_game():
    pygame.init()
    gm_set = Settings()

    screen = pygame.display.set_mode([gm_set.screen_width, gm_set.screen_height])
    pygame.display.set_caption(gm_set.caption)
    
    player = Player(screen)
    bubbles = pygame.sprite.Group()

    
    while True:
        gf.check_events(gm_set, screen, player, bubbles)
        player.update()
        bubbles.update()
        gf.update_screen(gm_set, screen, player, bubbles)
    
run_game()