import pygame
from scripts.helpers.all_enums import UserInputOptions

def wait_user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return UserInputOptions.QUIT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_a:  # Check if the spacebar is pressed
                return UserInputOptions.NEXT
            elif event.key == pygame.K_ESCAPE:  # Check for ESC key
                return UserInputOptions.ESC  # Exit if user confirms to quit
