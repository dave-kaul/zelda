import pygame
from settings import Settings
from link import Link
from background import Background
from heart import Heart

class Zelda:
    """Overall class to manage the Zelda game."""
    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()

        # Initialize the mixer for music
        pygame.mixer.init()

        # Load and play background music
        pygame.mixer.music.load('media/zelda.mp3')  # Replace with your music file path
        pygame.mixer.music.set_volume(0.8)  # Set volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Loop indefinitely

        # Game settings
        self.settings = Settings()

        # Screen setup
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Zelda")

        # Initialize joystick (Xbox controller)
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        # Initialize game objects
        self.link = Link(self)
        self.background = Background(self)
        self.hearts = pygame.sprite.Group()

        # Timer for Hearts
        self.heart_spawn_time = 500 # 1000 for Every 1 second for 1000, every half second for 500
        pygame.time.set_timer(pygame.USEREVENT, self.heart_spawn_time)


        # Sound
        self.collision_sound = pygame.mixer.Sound('media/collect.wav')

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()
            self.hearts.update()
            self.link.update()
            self.background.update()
            self.clock.tick(60)
            

            # Check for collisions between Link and hearts
            collisions = pygame.sprite.spritecollide(self.link, self.hearts, True)
            if collisions == True:
                self.collision_sound.play()  # Play collision sound

            self._update_screen()

    def _add_heart(self):
        """ Add new Heart to Game"""
        new_heart = Heart(self)
        self.hearts.add(new_heart)

    def _check_events(self):
        """Respond to keypresses and controller input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.USEREVENT:
                # Spawn new heart when timer event triggers
                self._add_heart()

         # Keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.link.moving_left = True
                elif event.key == pygame.K_RIGHT:
                  self.link.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                 self.link.moving_left = False
                elif event.key == pygame.K_RIGHT:
                  self.link.moving_right = False

         # Controller button input
            if self.joystick:
                if event.type == pygame.JOYBUTTONDOWN:
                    if self.joystick.get_button(0):  # A button
                        self.link.jump()

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen."""
        #self.screen.fill((0, 0, 0))  # Clear screen
        self.background.blitme()
        self.link.blitme()  # Draw Link
        self.hearts.draw(self.screen)  # Draw hearts
        pygame.display.flip()


if __name__ == '__main__':
    # Start the game
    game = Zelda()
    game.run_game()
