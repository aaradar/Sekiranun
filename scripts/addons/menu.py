 # menu.py
import pygame

def run_menu(screen):
    """Displays the menu screen."""
    # Initialize font and colors
    custom_font = "assets/fonts/sg.ttf"
    font = pygame.font.Font(custom_font, 72)  # Large font for title
    button_font = pygame.font.Font(custom_font, 48)  # Smaller font for buttons
    title_color = (255, 255, 255)
    button_color = (200, 200, 200)
    selected_color = (255, 255, 0)  # Highlighted button color
    background_color = (0, 0, 0)

    # Menu options
    menu_options = ["Start Game", "Exit"]
    selected_option = 0  # Tracks which option is highlighted

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Start Game":
                        return True  # Proceed to the game
                    elif menu_options[selected_option] == "Exit":
                        return False  # Exit the game
        
        # Draw the menu
        screen.fill(background_color)
        
        # Draw title
        title = font.render("Sekiranun", True, title_color)
        title_rect = title.get_rect(center=(screen.get_width() // 2, 150))
        screen.blit(title, title_rect)

        # Draw menu options
        for i, option in enumerate(menu_options):
            color = selected_color if i == selected_option else button_color
            text = button_font.render(option, True, color)
            text_rect = text.get_rect(center=(screen.get_width() // 2, 300 + i * 100))
            screen.blit(text, text_rect)
        
        # Update the display
        pygame.display.flip()
