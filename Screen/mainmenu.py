import pygame
import sys

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Initialize Pygame font module
pygame.font.init()
font = pygame.font.Font(None, FONT_SIZE)

def main_menu(screen, clock):
    play_icon = pygame.image.load('play.png')
    play_icon_rect = play_icon.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 1  # Change state to GAME
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if play_icon_rect.collidepoint(mouse_pos):
                        return 1  # Change state to GAME

        # Draw the Play icon
        play_icon_tinted = play_icon.copy()
        play_icon_tinted.fill(WHITE, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(play_icon_tinted, play_icon_rect)

        pygame.display.flip()
        clock.tick(60)
