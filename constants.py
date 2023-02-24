import pygame
import os
import threading
from skills import storm_gust


# Needed to use fonts and sounds
pygame.font.init() 
pygame.mixer.init()

# Set the window size
WIDTH, HEIGHT = 1920, 1200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ragnarok Onlite")

# Game Variables
FPS = 60
VEL = 20

# Colors
WHiTE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "prontera.png")), (WIDTH, HEIGHT))

# Window
def draw_window(player1_surf, player2_surf, player1_rect, player2_rect):
    WIN.blit(BG, (0, 0))
    WIN.blit(player1_surf, (player1_rect.x, player1_rect.y))
    WIN.blit(player2_surf, (player2_rect.x, player2_rect.y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # start drawing the spell circle asynchronously at the mouse click position
            center_pos = event.pos
            threading.Thread(target=storm_gust, args=(center_pos, WIN,)).start()
                

    pygame.display.update()