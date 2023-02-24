import pygame
from pygame.locals import *
from movement import player1_handle_movement, player2_handle_movement
from character import PLAYER1, PLAYER2, player1_coords, player2_coords
from constants import FPS, WIN, draw_window

# Setup the clock
clock = pygame.time.Clock()

# Main Loop
def main():
    pygame.init()
    
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            
        
        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed, player1_coords)
        player2_handle_movement(keys_pressed, player2_coords)
        
        draw_window(PLAYER1, PLAYER2, player1_coords, player2_coords)
        
    main()

if __name__ == "__main__":
    main()