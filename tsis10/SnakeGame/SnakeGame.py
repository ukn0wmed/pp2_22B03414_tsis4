import pygame
import random
import time
import psycopg2

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20

# Food properties
FOOD_SIZE = 20
MIN_WEIGHT = 1
MAX_WEIGHT = 5
DISAPPEAR_TIME = 5  # Food disappears after 5 seconds

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Load music file and play it indefinitely
pygame.mixer.music.load('bgmusic.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Snake class
class Snake:
    def __init__(self):
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (SNAKE_SPEED, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if self.grow:
            self.positions.insert(0, new_head)
            self.grow = False
        else:
            self.positions.pop()
            self.positions.insert(0, new_head)

    def change_direction(self, new_direction):
        dir_x, dir_y = self.direction
        new_dir_x, new_dir_y = new_direction

        if dir_x * new_dir_x + dir_y * new_dir_y == 0:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def shrink_snake(self):
        self.positions.pop()

    def collides_with_self(self):
        return self.positions[0] in self.positions[1:]

    def collides_with_wall(self):
        head_x, head_y = self.positions[0]
        return (
                head_x < 0
                or head_x >= WIDTH
                or head_y < 0
                or head_y >= HEIGHT
        )

    def draw(self, screen):
        for position in self.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))


# Food class
class Food:
    def __init__(self, snake_positions):
        self.position = self.generate_random_position(snake_positions)

    def generate_random_position(self, snake_positions):
        while True:
            x = random.randrange(0, WIDTH, FOOD_SIZE)
            y = random.randrange(0, HEIGHT, FOOD_SIZE)
            position = (x, y)

            if position not in snake_positions:
                return position
            self.position = position
            self.rect.x = position[0]
            self.rect.y = position[1]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))

# WeightedFood class
class WeightedFood(Food):
    def __init__(self, snake_positions):
        super().__init__(snake_positions)
        self.weight = random.randint(1, 3)  # Random weight between 1 to 3
        self.rect = pygame.Rect(self.position[0], self.position[1], FOOD_SIZE * self.weight, FOOD_SIZE * self.weight)
    def draw(self, screen):
        # Draw food with size proportional to its weight
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], FOOD_SIZE * self.weight, FOOD_SIZE * self.weight))

    # TimedFood class
class TimedFood(Food):
    def __init__(self, snake_positions):
        super().__init__(snake_positions)
        self.creation_time = pygame.time.get_ticks()  # Get the current time

    def is_expired(self):
        # Check if the food is expired
        return pygame.time.get_ticks() - self.creation_time > DISAPPEAR_TIME * 1000

# Poison class
class Poison:
    def __init__(self, snake_positions):
        self.position = self.generate_random_position(snake_positions)

    def generate_random_position(self, snake_positions):
        while True:
            x = random.randrange(0, WIDTH, FOOD_SIZE)
            y = random.randrange(0, HEIGHT, FOOD_SIZE)
            position = (x, y)
            if position not in snake_positions:
                return position

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, pygame.Rect(self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))


# Score and level counter
score = 0
level = 1

# Create snake and food
snake = Snake()
food = WeightedFood(snake.positions)  # Use WeightedFood
timed_food = TimedFood(snake.positions)  # Add timed_food object
poison = Poison(snake.positions)

# Database connection
conn = psycopg2.connect("dbname=snake user=postgres password=Ao511792")
cur = conn.cursor()

username = input("Enter your username: ")

# Check if user exists, if not insert them
cur.execute("SELECT * FROM users WHERE username = %s", (username,))
row = cur.fetchone()
if not row:
    cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()

# Check if user exists and get their level
cur.execute("SELECT level FROM users WHERE username = %s", (username,))
row = cur.fetchone()
if row:
    level = row[0]
else:
    level = 1  # Default level

cur.execute("SELECT score FROM users WHERE username = %s", (username,))
row = cur.fetchone()
if row:
    score = row[0]
else:
    score = 0  # Default score


# Game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change snake direction using arrow keys
        if not paused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -SNAKE_SPEED))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, SNAKE_SPEED))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-SNAKE_SPEED, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((SNAKE_SPEED, 0))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if paused:  # Add this
                paused = False
            else:
                paused = True  # Add this
                # Save score and level to database
                cur.execute("INSERT INTO user_scores (username, score, level) VALUES (%s, %s, %s)",
                            (username, score, level))
                conn.commit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False  # Add this

    if not paused:  # Add this
        snake.move()

    # Check if snake collides with food
    head_x, head_y = snake.positions[0]
    if food.rect.collidepoint(head_x, head_y):
        snake.grow_snake()
        food = WeightedFood(snake.positions)
        score += food.weight
        pygame.mixer.Sound('food.wav').play()

    # Check if snake collides with timed_food
    if snake.positions[0] == timed_food.position:
        snake.grow_snake()
        timed_food = TimedFood(snake.positions)
        score += 1
        pygame.mixer.Sound('food.wav').play()

        # Level up
        if score % 3 == 0:
            level += 1
            cur.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))
            conn.commit()
            clock.tick(10 + level * 2)  # Increase speed


    # Check if snake collides with poison
    if snake.positions[0] == poison.position:
        if len(snake.positions) > 1:
            snake.shrink_snake()
        else:
            running = False
        poison = Poison(snake.positions)
        pygame.mixer.Sound('poison.wav').play()

    # Check if snake collides with wall or itself
    if snake.collides_with_wall() or snake.collides_with_self():
        running = False

    screen.fill(WHITE)
    snake.draw(screen)
    food.draw(screen)
    timed_food.draw(screen)  # Draw timed_food
    poison.draw(screen)

    # Remove timed_food if expired
    if timed_food.is_expired():
        timed_food = TimedFood(snake.positions)

    # Display score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}", 1, BLACK)
    level_text = font.render(f"Level: {level}", 1, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(10 + level * 2)

if not running:
    cur.execute("UPDATE users SET level = %s WHERE username = %s", (level, username))
    conn.commit()

conn.close()

pygame.mixer.music.stop()

pygame.mixer.Sound('poison.wav').play()
# Game over message
font = pygame.font.Font(None, 50)
game_over_text = font.render("Game Over", 1, BLACK)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)

# Display final score
final_score_text = font.render(f"Final Score: {score}", 1, BLACK)
final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
screen.blit(final_score_text, final_score_rect)

# Update the display and wait for 3 seconds
pygame.display.update()
time.sleep(3)

# Quit Pygame
pygame.quit()
