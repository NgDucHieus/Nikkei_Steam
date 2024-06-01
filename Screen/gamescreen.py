import pygame
import sys

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 24
INPUT_BOX_HEIGHT = 40
PADDING = 10

# Initialize Pygame font module
pygame.font.init()
font = pygame.font.Font(None, FONT_SIZE)

def chat_screen(screen, clock):
    chat_history = []  # List to store chat messages
    input_text = ""  # Current input text
    input_box_rect = pygame.Rect(PADDING, screen.get_height() - INPUT_BOX_HEIGHT - PADDING, screen.get_width() - 2 * PADDING, INPUT_BOX_HEIGHT)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0  # Change state to MENU
                elif event.key == pygame.K_RETURN:
                    if input_text.strip():  # Avoid adding empty messages
                        chat_history.append(input_text)
                        input_text = ""  # Clear input box
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Delete last character
                else:
                    input_text += event.unicode  # Add typed character to input text

        # Draw chat history
        y_offset = PADDING
        for message in chat_history:
            text_surface = font.render(message, True, WHITE)
            screen.blit(text_surface, (PADDING, y_offset))
            y_offset += FONT_SIZE + PADDING

        # Draw input box
        pygame.draw.rect(screen, WHITE, input_box_rect, 2)
        input_surface = font.render(input_text, True, WHITE)
        screen.blit(input_surface, (input_box_rect.x + PADDING, input_box_rect.y + (INPUT_BOX_HEIGHT - FONT_SIZE) // 2))

        pygame.display.flip()
        clock.tick(60)
