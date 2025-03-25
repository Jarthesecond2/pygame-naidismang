import pygame
from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    pygame.init()
    gm_set = Settings()

    screen = pygame.display.set_mode([gm_set.screen_width, gm_set.screen_height])
    pygame.display.set_caption(gm_set.caption)
    
    player = Player(screen)

    while True:
        
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_set, screen, player)
    
run_game()