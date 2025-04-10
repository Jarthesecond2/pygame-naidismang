"""Game"""
import pygame
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf

def run_game():
    pygame.init()
    gm_set = Settings()

    screen = pygame.display.set_mode([gm_set.screen_width, gm_set.screen_height])
    pygame.display.set_caption(gm_set.caption)

    play_button = Button(gm_set, screen, "Play")
    
    stats = GameStats()
    
    sb = Scoreboard(gm_set, screen, stats)

    clock = pygame.time.Clock()

    player = Player(screen)

    bubbles = pygame.sprite.Group()

    
    while True:
        gf.check_events(gm_set, screen, player, bubbles, stats, play_button)
        if  stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb, gm_set)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_set, screen, player, bubbles, clock, stats, play_button, sb)
    
run_game()