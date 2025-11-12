import pygame
import sys

sponge = pygame.image.load("assets/images/sponge.png")
imagerect = sponge.get_rect()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


# Initialize Pygame
pygame.init()

font = pygame.font.Font('assets/fonts/main.ttf', 31)

# Window size
WIDTH, HEIGHT = 800, 600

# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Frame")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((30, 30, 30))

    # This block generates an image
    screen.blit(sponge, imagerect)

    # This is where we make a text box
    text = font.render('freakbob', True, white, (30,30,30))
    textbox = text.get_rect()
    textbox.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textbox)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

# Quit Pygame safely
pygame.quit()
sys.exit()
