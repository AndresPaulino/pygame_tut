import pygame
from constants import WIDTH, HEIGHT, VEL

# Handle character movement
def player1_handle_movement(keys_pressed, player1):
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0: # UP
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL + player1.height < HEIGHT: # DOWN
        player1.y += VEL
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0: # LEFT
        player1.x -= VEL
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < WIDTH: # RIGHT
        player1.x += VEL
        
def player2_handle_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_i] and player2.y - VEL > 0: # UP
        player2.y -= VEL
    if keys_pressed[pygame.K_k] and player2.y + VEL + player2.height < HEIGHT: # DOWN
        player2.y += VEL
    if keys_pressed[pygame.K_j] and player2.x - VEL > 0: # LEFT
        player2.x -= VEL
    if keys_pressed[pygame.K_l] and player2.x + VEL + player2.height < WIDTH: # RIGHT
        player2.x += VEL