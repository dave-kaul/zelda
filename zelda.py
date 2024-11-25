import pygame
from settings import Settings
from link import Link
from background import ParallaxBackground
from collectible import Collectible

class Zelda:
    """Overall class to manage the Zelda game."""
    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()

        # Initialize the mixer for music
        pygame.mixer.init()

        # Game settings
        self.settings = Settings()

        # Load and play background music
        pygame.mixer.music.load(self.settings.main_music) 
        pygame.mixer.music.set_volume(0.8)  # Set volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Loop indefinitely

        


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
        self.background = ParallaxBackground(self)
        self.collectibles = pygame.sprite.Group()

        # Timer for Collectibles
        
        pygame.time.set_timer(pygame.USEREVENT, self.settings.collectible_spawn_time)


        # Sound
        self.collect_sound = pygame.mixer.Sound(self.settings.collect_sound)
        pygame.mixer.music.set_volume(.5)
        

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()
            self.background.update()
            self.link.update()
            self.collectibles.update()
            self._update_screen()
            
            self.clock.tick(60)
            

            # Check for collisions between Link and collectibles
            collisions = pygame.sprite.spritecollide(self.link, self.collectibles, True)
            if collisions:
                self.collect_sound.set_volume(0.5)
                self.collect_sound.play()  # Play collision sound
                #print ("collectible sound")
                

            self._update_screen()

    def _add_collectible(self):
        """ Add new Collectible to Game"""
        new_collectible = Collectible(self)
        self.collectibles.add(new_collectible)

    def _check_events(self):
        """Respond to keypresses and controller input."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:   #Check if close box at top right is clicked
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # Check if ESC key is pressed
                print ('quit')
                pygame.quit()
                exit()
            elif event.type == pygame.USEREVENT:
                # Spawn new collectible when timer event triggers
                self._add_collectible()

         # Keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.link.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.link.moving_right = True
                elif event.key == pygame.K_SPACE:
                    self.link.is_jumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                 self.link.moving_left = False
                elif event.key == pygame.K_RIGHT:
                  self.link.moving_right = False
                elif event.key == pygame.K_d:  # 'D' key to dash
                    self.link.dash()

         # Controller button input
            if self.joystick:
                if event.type == pygame.JOYBUTTONDOWN:
                    if self.joystick.get_button(0):  # A button will jump
                        self.link.jump()
                    if self.joystick.get_button(3): # y button will quit
                        pygame.quit()
                        exit()
                    if self.joystick.get_button(1): # b button will dash
                        self.link.dash()
                   

    def _update_screen(self):
        """Update the images on the screen and flip to the new screen."""
        
        self.background.blitme()
        self.link.blitme()  # Draw Link
        self.collectibles.draw(self.screen)  # Draw collectibles
        pygame.display.flip()


if __name__ == '__main__':
    # Start the game
    game = Zelda()
    game.run_game()
