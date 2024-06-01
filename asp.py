import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 24
INPUT_BOX_HEIGHT = 40
MARGIN = 10

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Turing Test')

# Setup the clock
clock = pygame.time.Clock()

# Setup font
pygame.font.init()
font = pygame.font.Font(None, FONT_SIZE)

# Chatbot responses (simple hardcoded responses for demonstration)
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm a program, so I don't have feelings, but I'm here to help!",
    "what is your name": "I am a chatbot created for this Turing Test simulation.",
    "exit": "Goodbye! Have a great day!"
}

def get_response(user_input):
    # Simple logic to return a response based on user input
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def turing_test():
    chat_history = []  # List to store chat messages
    input_box_text = ""  # Text entered in the input box

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_box_text.strip():  # Only add non-empty messages
                        chat_history.append(("User", input_box_text))
                        response = get_response(input_box_text)
                        chat_history.append(("Chatbot", response))
                        if input_box_text.lower() == "exit":
                            return
                        input_box_text = ""  # Clear input box after sending message
                elif event.key == pygame.K_BACKSPACE:
                    input_box_text = input_box_text[:-1]  # Delete last character
                else:
                    input_box_text += event.unicode  # Add typed character to input box

        # Draw chat history
        y_offset = 10
        for speaker, message in chat_history:
            text_surface = font.render(f"{speaker}: {message}", True, WHITE)
            screen.blit(text_surface, (MARGIN, y_offset))
            y_offset += FONT_SIZE + 5

        # Draw input box
        pygame.draw.rect(screen, WHITE, (MARGIN, screen.get_height() - INPUT_BOX_HEIGHT - MARGIN, 
                                         screen.get_width() - 2 * MARGIN, INPUT_BOX_HEIGHT), 2)
        input_text_surface = font.render(input_box_text, True, WHITE)
        screen.blit(input_text_surface, (MARGIN + 5, screen.get_height() - INPUT_BOX_HEIGHT - MARGIN + 5))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    turing_test()
