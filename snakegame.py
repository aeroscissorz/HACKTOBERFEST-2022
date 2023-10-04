import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize variables
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed_x = 0
snake_speed_y = 0
snake_body = []
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed_x = 0
                snake_speed_y = -SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_speed_x = 0
                snake_speed_y = SNAKE_SIZE
            if event.key == pygame.K_LEFT:
                snake_speed_x = -SNAKE_SIZE
                snake_speed_y = 0
            if event.key == pygame.K_RIGHT:
                snake_speed_x = SNAKE_SIZE
                snake_speed_y = 0

    # Move the snake
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # Check for collision with the wall
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False

    # Check for collision with itself
    if (snake_x, snake_y) in snake_body:
        running = False

    # Add the new head to the snake's body
    snake_body.append((snake_x, snake_y))

    # Check if the snake ate the food
    food_x, food_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x, food_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)
    else:
        snake_body.pop(0)

    # Draw everything
    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Game over
font = pygame.font.Font(None, 36)
text = font.render(f"Game Over - Score: {score}", True, RED)
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a moment before closing
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
