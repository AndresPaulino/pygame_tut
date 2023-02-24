import pygame
import os
from constants import WIDTH, HEIGHT

# Sprite dimensions
SPRITE_HEIGHT = 128
SPRITE_WIDTH = 128

SPRITE_SPAWN_X = WIDTH // 2 - SPRITE_WIDTH // 2
SPRITE_SPAWN_Y = HEIGHT // 2 - SPRITE_HEIGHT // 2

# Players
# Character sprite sheet
character_sprite_sheet = pygame.image.load(os.path.join("Assets", "Characters", "character_spritesheet.png"))

# Player
def get_player_surface(direction):
    if direction == "up":
        return pygame.transform.scale(character_sprite_sheet.subsurface(0, 48, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))
    elif direction == "down":
        return pygame.transform.scale(character_sprite_sheet.subsurface(0, 0, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))
    elif direction == "left":
        return pygame.transform.scale(character_sprite_sheet.subsurface(0, 96, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))
    elif direction == "right":
        return pygame.transform.scale(character_sprite_sheet.subsurface(0, 144, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))
    
# Player rect
player1_rect = pygame.Rect(SPRITE_SPAWN_X, SPRITE_SPAWN_Y, SPRITE_WIDTH, SPRITE_HEIGHT)