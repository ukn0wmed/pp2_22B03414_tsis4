import pygame

# Initialize Pygame and set up the screen
pygame.init()
width = 900
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

# Set up the ball
ball_x = 295
ball_y = 215
ball_radius = 25

# Define the colors
white = (255, 255, 255)
red = (255, 0, 0)

# Start the main loop of the program
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, exit the program
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # If the user presses the Escape key, exit the program
                pygame.quit()
                exit()
            elif event.key == pygame.K_UP:
                if ball_y > ball_radius:
                    ball_y -= 20
            elif event.key == pygame.K_DOWN:
                if ball_y < 480 - ball_radius:
                    ball_y += 20
            elif event.key == pygame.K_LEFT:
                if ball_x > ball_radius:
                    ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_x < 640 - ball_radius:
                    ball_x += 20

    # Draw the background and the ball
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Update the screen
    pygame.display.update()