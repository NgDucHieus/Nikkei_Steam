import pygame
import sys
from Screen.gamescreen import chat_screen
from Screen.mainmenu import main_menu

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Main Menu')

# Setup the clock
clock = pygame.time.Clock()

# Game states
MENU = 0
GAME = 1

# Initial game state
game_state = MENU

if __name__ == '__main__':
    while True:
        if game_state == MENU:
            game_state = main_menu(screen, clock)
        elif game_state == GAME:
            game_state = chat_screen(screen, clock)
