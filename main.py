import pygame
from pygame.locals import *
from movement import *
from character import *
from constants import FPS, draw_window

# Setup the clock
clock = pygame.time.Clock()

# Main Game Loop
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
        def handle_direction_change():
            default_direction = "down"
            direction = player1_handle_movement(keys_pressed, player1_rect, default_direction)
            return direction
        
        player_surface = get_player_surface(handle_direction_change())
        
        draw_window(player_surface, player1_rect)
        
    main()

if __name__ == "__main__":
    main()