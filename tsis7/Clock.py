import pygame
import time

pygame.init()

# Set up the window
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simple Clock")

# Load images
background = pygame.image.load("zadnik.png")
minute_hand = pygame.image.load("levayaruka.png")
second_hand = pygame.image.load("proverka.png")

# Calculate hand size
hand_size = min(size) // 2

# Scale hands
minute_hand_scaled = pygame.transform.scale(minute_hand, (hand_size, hand_size))
second_hand_scaled = pygame.transform.scale(second_hand, (hand_size, hand_size))

# Set up the clock
clock = pygame.time.Clock()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.blit(background, (0, 0))

    # Get the current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Rotate the hands
    minute_angle = (60 - minutes) * 6
    minute_hand_rotated = pygame.transform.rotate(minute_hand_scaled, minute_angle)
    second_angle = (60 - seconds) * 6
    second_hand_rotated = pygame.transform.rotate(second_hand_scaled, second_angle)

    # Draw the hands
    screen.blit(minute_hand_rotated, (200 - minute_hand_rotated.get_width() // 2, 200 - minute_hand_rotated.get_height() // 2))
    screen.blit(second_hand_rotated, (200 - second_hand_rotated.get_width() // 2, 200 - second_hand_rotated.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)