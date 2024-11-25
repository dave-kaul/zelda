import pygame
import random


class Collectible(pygame.sprite.Sprite):
    """Class to manage collectibles in the game."""
    def __init__(self, zelda_game):
        """Initialize the heart and set its starting position."""
        super().__init__()
        self.screen = zelda_game.screen
        self.settings = zelda_game.settings

        # Load heart image
        self.image = pygame.image.load(self.settings.collectible)
        self.image = pygame.transform.scale(self.image, (30, 30))  # Scale to 30 pixels by 30 pixels
        self.rect = self.image.get_rect()

        # Randomize heart position
        self.rect.x = random.randint(700, self.screen.get_width() - self.rect.width)
        # Adjust Y value to heights that Link can reach
        self.rect.y = random.randint(350, self.screen.get_height() - self.rect.height - 100)

        # Reference to the background scroll speed
        #self.scroll_speed = zelda_game.settings.background.scroll_speed

    def update(self):
        """Move the heart in sync with the background."""
        # Move the heart to the left along with the background
        self.rect.x -= self.settings.layer4_speed
        # Remove the heart if it goes off-screen
        if self.rect.right < 0:
            self.kill()
    
