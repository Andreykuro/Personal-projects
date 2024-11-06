import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.5
JUMP_STRENGTH = -10
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT - 60
        self.width = 50
        self.height = 50
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True

    def update(self):
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        # Check for ground collision
        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - 60
        self.width = 50
        self.height = 50

    def update(self):
        self.x -= 5  # Move the obstacle left

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Main game function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Parkour Game")

    clock = pygame.time.Clock()
    player = Player()
    obstacles = []
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Update player
        player.update()

        # Create obstacles
        if len(obstacles) == 0 or obstacles[-1].x < SCREEN_WIDTH - 300:
            obstacles.append(Obstacle())

        # Update and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.x < -obstacle.width:
                obstacles.remove(obstacle)
                score += 1  # Increment score when obstacle is passed
            if (player.x < obstacle.x + obstacle.width and
                player.x + player.width > obstacle.x and
                player.y + player.height > obstacle.y):
                running = False  # Collision detected

            obstacle.draw(screen)

        # Draw player
        player.draw(screen)

        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()