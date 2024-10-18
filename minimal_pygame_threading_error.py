import pygame
import threading


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Robot Simulator")

def run_simulation():
    # Start the Pygame rendering loop
    clock = pygame.time.Clock()
    while True:
        pygame.display.flip()
        # Cap the frame rate to 60 FPS
        clock.tick(60)

threading.Thread(target=run_simulation, daemon=True).start()