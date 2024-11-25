#import pygame

class Settings:
    """ A class to store all settings"""

    def __init__(self):
        """ Initialze the game's settings"""
        # Set width of screen
        self.screen_width = 1850
        self.screen_height = 655
        self.bg_color = ((0,0,0))

    
        # Settings for Link
        self.link_speed = 15
        self.gravity = 1
        self.jump_velocity = 16  # Initial upward velocity

        # Dash properties
        self.is_dashing = False
        self.dash_duration = 10  # Dash lasts 10 frames
        self.dash_timer = 0
        self.dash_speed = 30  # Speed during dash
        self.dash_cooldown = 1  # Cooldown time before next dash
        self.cooldown_timer = 0

        self.collectible_spawn_time = 500

        # Parallax scrolling speeds
        self.layer1_speed = 1  # clouds
        self.layer2_speed = 2  # back trees
        self.layer3_speed = 3  # small trees
        self.layer4_speed = 5  # Fground

        self.main_music = 'media/zelda.mp3'
        self.collect_sound = 'media/collect.wav'
        self.jump_sound = 'media/link_jump.wav'
        self.collectible = 'media/heart.png'
        self.link_image = 'media/link.png'
        
        



        