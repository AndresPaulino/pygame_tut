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

PLAYER1 = pygame.transform.scale(character_sprite_sheet.subsurface(0, 0, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))
PLAYER2 = pygame.transform.scale(character_sprite_sheet.subsurface(0, 64, 32, 32), (SPRITE_HEIGHT, SPRITE_WIDTH))

player1_coords = pygame.Rect(SPRITE_SPAWN_X, SPRITE_SPAWN_Y, SPRITE_HEIGHT, SPRITE_WIDTH)
player2_coords = pygame.Rect(SPRITE_SPAWN_X, SPRITE_SPAWN_Y, SPRITE_HEIGHT, SPRITE_WIDTH)


