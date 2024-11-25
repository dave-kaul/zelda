import pygame

class Link:
    """Class to manage Link."""
    def __init__(self, zelda_game):
        """Initialize Link and set its starting position."""
        self.screen = zelda_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = zelda_game.settings

        # Load Link's images and initialize rect
        self.image_right = pygame.image.load(self.settings.link_image)  # Default image facing right
        self.image_left = pygame.transform.flip(self.image_right, True, False)  # Flipped image for facing left
        self.image_right = pygame.transform.scale(self.image_right, (130, 100))
        self.image_left = pygame.transform.scale(self.image_left, (130, 100))
        self.image = self.image_right
        self.rect = self.image.get_rect()

        # Position Link slightly above the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 80  # Offset from bottom
        self.ground_y = self.rect.bottom

        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self.is_jumping = False

        # Dashing
        self.is_dashing = False

        # Jump mechanics
        self.jump_velocity = self.settings.jump_velocity  # Initial jump velocity
        self.gravity = self.settings.gravity  # Gravity effect

        # Joystick reference
        self.joystick = zelda_game.joystick

        # Direction tracking
        self.facing_left = False

        # Load jump sound
        self.jump_sound = pygame.mixer.Sound(self.settings.jump_sound)
        self.jump_sound.set_volume(0.5)

    def update(self):
        """Update Link's position based on movement flags and joystick input."""


        # Handle dash movement
        if self.is_dashing:
            if self.settings.dash_timer > 0:
                self.rect.x += self.settings.dash_speed if not self.facing_left else -self.settings.dash_speed
                self.settings.dash_timer -= 1
            else:
                self.is_dashing = False
                self.settings.cooldown_timer = self.settings.dash_cooldown


        # Horizontal movement
        elif self.settings.cooldown_timer == 0:
            if self.moving_left and self.rect.left > 0:
                self.rect.x -= self.settings.link_speed
                self.facing_left = True
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.x += self.settings.link_speed
                self.facing_left = False

         # Decrease cooldown timer if it's active
        if self.settings.cooldown_timer > 0:
            self.settings.cooldown_timer -= 1

        # Joystick horizontal movement
        if self.joystick:
            axis_x = self.joystick.get_axis(0)  # Get horizontal axis
            if abs(axis_x) > 0.1:  # Ignore joystick drift
                self.rect.x += int(axis_x * self.settings.link_speed)
                self.facing_left = axis_x < 0

        # Handle jumping
        if self.is_jumping:
            self.rect.y -= self.jump_velocity  # Move upward
            self.jump_velocity -= self.gravity  # Apply gravity

            # Check if Link has landed
            if self.rect.bottom >= self.screen_rect.bottom - 80:
                self.rect.bottom = self.screen_rect.bottom - 80  # 80 makes sure Link is not a bottom of screen
                self.is_jumping = False
                self.jump_velocity = self.settings.jump_velocity  # Reset jump velocity

    def jump(self):
        """Make Link jump with horizontal velocity based on movement."""
        if not self.is_jumping:  # Only jump if not already in the air
            self.is_jumping = True
            self.jump_sound.play()  # Play jump sound

    def dash(self):
        """Activate the dash mechanic."""
        if not self.is_dashing and self.settings.cooldown_timer == 0:
            self.is_dashing = True
            self.settings.dash_timer = self.settings.dash_duration

    def blitme(self):
        """Draw Link at its current location."""
        if self.facing_left:
            self.image = self.image_right
        else:
            self.image = self.image_left
        self.screen.blit(self.image, self.rect)
