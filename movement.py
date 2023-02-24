import pygame
from constants import WIDTH, HEIGHT, VEL

# Handle character movement
def player1_handle_movement(keys_pressed, player1, direction):
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0: # UP
        player1.y -= VEL
        direction = "up"
    if keys_pressed[pygame.K_s] and player1.y + VEL + player1.height < HEIGHT: # DOWN
        player1.y += VEL
        direction = "down"
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0: # LEFT
        player1.x -= VEL
        direction = "left"
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < WIDTH: # RIGHT
        player1.x += VEL
        direction = "right"
    return direction
        