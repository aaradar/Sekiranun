import pygame

def run_intro(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to My VN Game!", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (200, 300))
