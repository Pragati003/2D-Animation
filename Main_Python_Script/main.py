import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Animation with Collision Detection")

# Load images
background = pygame.image.load("background.jpg")  # Background image
movable_image = pygame.image.load("movable.png")  # Movable object
movable_rect = movable_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Load beep sound
beep_sound = pygame.mixer.Sound("beep.wav")

# Movement speed
SPEED = 5

# Main loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(movable_image, movable_rect)  # Draw movable image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        movable_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        movable_rect.x += SPEED
    if keys[pygame.K_UP]:
        movable_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        movable_rect.y += SPEED

    # Collision detection
    if movable_rect.left <= 0 or movable_rect.right >= SCREEN_WIDTH or \
       movable_rect.top <= 0 or movable_rect.bottom >= SCREEN_HEIGHT:
        beep_sound.play()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
