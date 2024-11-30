import pygame
from scripts.scenes.intro import run_intro

def start_game():
    pygame.init()
    
    # Settings
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("My VN Game")
    clock = pygame.time.Clock()
    
    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Example: Run intro scene
        run_intro(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    start_game()
