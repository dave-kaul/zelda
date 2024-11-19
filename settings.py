class Settings:
    """ A class to store all settings"""

    def __init__(self):
        """ Initialze the game's settings"""
        # Set width of screen
        self.screen_width = 1400
        self.screen_height = 655
        #self.bg_color = ((0,0,0))

        # background scroll speed is set here
        self.background_scroll_speed = 2


        # Settings for Link
        self.link_speed = 7

        self.gravity = 1
        self.jump_velocity = 18  # Initial upward velocity

        self.heart_spawn_time = 12


        