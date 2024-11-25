import pygame

class ParallaxBackground:
    """Class to manage a parallax scrolling background."""
    def __init__(self, zelda_game):
        """Initialize the parallax background."""
        self.screen = zelda_game.screen
        self.settings = zelda_game.settings

        # Load the background layers
        self.layer1 = pygame.image.load('media/background_clouds.png').convert_alpha()
        self.layer2 = pygame.image.load('media/background_forest.png').convert_alpha()
        self.layer3 = pygame.image.load('media/background_trees_only.png').convert_alpha()
        self.layer4 = pygame.image.load('media/background_ground_only.png').convert_alpha()

        # Get rects for each layer
        self.rect1 = self.layer1.get_rect()
        self.rect2 = self.layer2.get_rect()
        self.rect3 = self.layer3.get_rect()
        self.rect4 = self.layer3.get_rect()

        # Create duplicate rects for seamless scrolling
        self.rect1_copy = self.rect1.copy()
        self.rect2_copy = self.rect2.copy()
        self.rect3_copy = self.rect3.copy()
        self.rect4_copy = self.rect3.copy()

        # Position duplicate rects to the right of the originals
        self.rect1_copy.left = self.rect1.right
        self.rect2_copy.left = self.rect2.right
        self.rect3_copy.left = self.rect3.right
        self.rect4_copy.left = self.rect4.right

    def update(self):
        """Update the position of each layer for scrolling."""
        # Layer 1: Slowest
        self.rect1.x -= self.settings.layer1_speed
        self.rect1_copy.x -= self.settings.layer1_speed

        # Layer 2: Medium
        self.rect2.x -= self.settings.layer2_speed
        self.rect2_copy.x -= self.settings.layer2_speed

        # Layer 3: Fastest
        self.rect3.x -= self.settings.layer3_speed
        self.rect3_copy.x -= self.settings.layer3_speed

        # Layer 3: Fastest
        self.rect4.x -= self.settings.layer4_speed
        self.rect4_copy.x -= self.settings.layer4_speed

        # Reset positions for seamless scrolling
        if self.rect1.right <= 0:
            self.rect1.left = self.rect1_copy.right
        if self.rect1_copy.right <= 0:
            self.rect1_copy.left = self.rect1.right

        if self.rect2.right <= 0:
            self.rect2.left = self.rect2_copy.right
        if self.rect2_copy.right <= 0:
            self.rect2_copy.left = self.rect2.right

        if self.rect3.right <= 0:
            self.rect3.left = self.rect3_copy.right
        if self.rect3_copy.right <= 0:
            self.rect3_copy.left = self.rect3.right

        if self.rect4.right <= 0:
            self.rect4.left = self.rect4_copy.right
        if self.rect4_copy.right <= 0:
            self.rect4_copy.left = self.rect4.right

    def blitme(self):
        """Draw the background layers."""
        
        self.screen.blit(self.layer1, self.rect1)
        self.screen.blit(self.layer1, self.rect1_copy)

        self.screen.blit(self.layer2, self.rect2)
        self.screen.blit(self.layer2, self.rect2_copy)

        self.screen.blit(self.layer3, self.rect3)
        self.screen.blit(self.layer3, self.rect3_copy)

        self.screen.blit(self.layer4, self.rect4)
        self.screen.blit(self.layer4, self.rect4_copy)


        

