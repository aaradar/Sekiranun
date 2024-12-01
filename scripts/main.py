import pygame
from scripts.addons.menu import run_menu
from scripts.addons.exit_screen import show_exit_dialog
from scripts.scenes.intro import run_intro

def start_game():
    pygame.init()
    
    # Settings
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sekiranun")
    clock = pygame.time.Clock()

    # Run menu screen
    if not run_menu(screen):
        pygame.quit()
        return

    # Run intro scene after menu
    run_intro(screen)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Show exit dialog when ESC is pressed
                if show_exit_dialog(screen):
                    running = False

        # Example placeholder for game content
        screen.fill((0, 0, 50))  # Placeholder background color

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    start_game()
