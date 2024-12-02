import pygame

class Character:
    def __init__(self, character_file, scale_factor=0.5):
        """
        Initializes the Character object by loading and scaling the character image.

        :param character_file: Path to the character image file.
        :param scale_factor: Factor by which to scale the character image.
        """
        self.character = pygame.image.load(character_file)

        # Get the original dimensions of the image
        original_width, original_height = self.character.get_width(), self.character.get_height()
        self.new_width = int(original_width * scale_factor)
        self.new_height = int(original_height * scale_factor)

        # Scale the image
        self.character = pygame.transform.scale(self.character, (self.new_width, self.new_height))

    def display(self, screen, x, y):
        """
        Displays the character on the screen at the given position.

        :param screen: The pygame screen to display the character on.
        :param x: X-coordinate of the character's position.
        :param y: Y-coordinate of the character's position.
        """
        screen.blit(self.character, (x, y))

    def displayCenter(self, screen):
        """
        Displays the character on the center of the screen.

        :param screen: The pygame screen to display the character on.
        """
        character_x = (screen.get_width() - self.character.get_width()) // 2
        character_y = (screen.get_height() - self.character.get_height()) // 2
        screen.blit(self.character, (character_x, character_y))

