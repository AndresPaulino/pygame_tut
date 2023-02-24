import pygame

YELLOW = (255, 255, 0)

# Function to draw the spell circle
def storm_gust(center_pos, WIN):
    spell_radius = 50
    spell_time = 3000  # in milliseconds
    spell_start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - spell_start_time <= spell_time:
        # draw the spell circle at the center position
        pygame.draw.circle(WIN, YELLOW, center_pos, spell_radius, 5)

        # update the display
        pygame.display.update()

        # maintain the desired frame rate
        pygame.time.delay(10)
            
            
            
        
         