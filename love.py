import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I Love You")

clock = pygame.time.Clock()

# Warna
BLACK = (5, 5, 20)
WHITE = (255, 255, 255)
PINK = (255, 20, 147)
GREEN = (0, 180, 120)
YELLOW = (255, 255, 100)

font_big = pygame.font.SysFont("Arial", 40, bold=True)

# Partikel bintang
stars = []
for _ in range(100):
    stars.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    ])

# Partikel cinta
love_particles = []

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bintang
    for star in stars:
        pygame.draw.circle(screen, WHITE, (star[0], star[1]), star[2])

    # Judul
    text = font_big.render("I Love You", True, WHITE)
    screen.blit(text, (90, 80))

    # Batang bunga
    pygame.draw.line(screen, GREEN, (120, 500), (120, 350), 8)
    pygame.draw.line(screen, GREEN, (200, 550), (200, 300), 8)
    pygame.draw.line(screen, GREEN, (280, 500), (280, 360), 8)

    # Daun
    pygame.draw.ellipse(screen, GREEN, (90, 420, 40, 20))
    pygame.draw.ellipse(screen, GREEN, (170, 450, 40, 20))
    pygame.draw.ellipse(screen, GREEN, (250, 420, 40, 20))

    # Fungsi bunga
    def flower(x, y):
        for angle in range(0, 360, 72):
            px = x + math.cos(math.radians(angle)) * 25
            py = y + math.sin(math.radians(angle)) * 25
            pygame.draw.circle(screen, (180,255,230), (int(px), int(py)), 18)

        pygame.draw.circle(screen, YELLOW, (x, y), 15)

    flower(120, 330)
    flower(200, 280)
    flower(280, 340)

    # Efek love
    if random.randint(1, 5) == 1:
        love_particles.append([
            random.randint(50, 350),
            HEIGHT,
            random.randint(2, 5)
        ])

    for particle in love_particles:
        particle[1] -= 2
        pygame.draw.circle(screen, PINK, (particle[0], particle[1]), particle[2])

    pygame.display.update()
    clock.tick(60)

pygame.quit()