import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.get_rect()

        #Load the ship image and gets its rect.
        self.image = pygame.image.loag('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom cent of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)