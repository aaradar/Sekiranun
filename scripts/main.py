import pygame
from scripts.addons.menu import run_menu
from scripts.scenes.intro import run_intro
from scripts.scenes.chapter1 import chapter1

def start_game():
    pygame.init()
    
    # Settings
    # Load your custom icon image
    icon = pygame.image.load('assets/icon/icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sekiranun")
    clock = pygame.time.Clock()


    running = True
    while running:
        # Run menu screen
        menuSelection = run_menu(screen)    

        # Run intro scene after menu
        if menuSelection == 1:
            running = False
        elif menuSelection == 0:
            run_intro(screen)

            chapter1(screen)
        


        
        
        


    pygame.quit()

if __name__ == "__main__":
    start_game()
