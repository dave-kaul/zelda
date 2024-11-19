import pygame

class Background:
    """Class to manage a horizontally scrolling background."""
    def __init__(self, zelda_game):
        """Initialize the background."""
        self.screen = zelda_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = zelda_game.settings # Access settings

        # Load the background image
        self.image = pygame.image.load('media/background_forest.png')  # Replace with your background image
        self.rect = self.image.get_rect()

        # Create two copies of the background for seamless scrolling
        self.rect1 = self.rect.copy()
        self.rect2 = self.rect.copy()
        self.rect2.left = self.rect1.right  # Position the second background to the right of the first

        # Scrolling speed
        #self.scroll_speed = 2  # Adjust speed as needed

    def update(self):
        """Update the position of the background for scrolling."""
        # Move both background rects to the left
        self.rect1.x -= self.settings.background_scroll_speed
        self.rect2.x -= self.settings.background_scroll_speed

        # Reset position if a rect goes off-screen
        if self.rect1.right <= 0:  # If rect1 moves off the screen
            self.rect1.left = self.rect2.right
        if self.rect2.right <= 0:  # If rect2 moves off the screen
            self.rect2.left = self.rect1.right

    def blitme(self):
        """Draw the background."""
        self.screen.blit(self.image, self.rect1)
        self.screen.blit(self.image, self.rect2)
