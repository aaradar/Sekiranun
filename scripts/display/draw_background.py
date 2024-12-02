import pygame

def display_background(screen, backgroundFile):
    background = pygame.image.load(backgroundFile)
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))