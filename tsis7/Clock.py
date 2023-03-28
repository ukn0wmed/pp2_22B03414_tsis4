import pygame
import datetime

# Initialize Pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mickey Clock")

# Load the image of Mickey and set the size of the clock
mickey_image = pygame.image.load("mickeyclock.jpeg").convert()
mickey_rect = mickey_image.get_rect()
clock_size = min(mickey_rect.width, mickey_rect.height)

# Set up the fonts
font = pygame.font.SysFont(None, 40)
font_color = (255, 255, 255)

# Start the main loop of the program
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, exit the program
            pygame.quit()
            exit()

    # Get the current time
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    # Calculate the rotation angle for the seconds hand
    seconds_angle = 360 * seconds / 60
    seconds_hand = pygame.transform.rotate(mickey_image.subsurface(117, 26, 18, 75), seconds_angle)

    # Calculate the rotation angle for the minutes hand
    minutes_angle = 360 * minutes / 60
    minutes_hand = pygame.transform.rotate(mickey_image.subsurface(86, 21, 23, 81), minutes_angle)

    # Draw the clock and the hands
    screen.fill((0, 0, 0))
    mickey_rect.center = (250, 250)
    mickey_image_scaled = pygame.transform.smoothscale(mickey_image, (clock_size, clock_size))
    screen.blit(mickey_image_scaled, mickey_rect)
    seconds_rect = seconds_hand.get_rect(center=mickey_rect.center)
    screen.blit(seconds_hand, seconds_rect)
    minutes_rect = minutes_hand.get_rect(center=mickey_rect.center)
    screen.blit(minutes_hand, minutes_rect)

    # Display the current time in the top left corner
    time_text = font.render(now.strftime("%H:%M:%S"), True, font_color)
    screen.blit(time_text, (10, 10))

    # Update the screen
    pygame.display.update()
