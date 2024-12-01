# exit_dialogue.py
import pygame

def show_exit_dialog(screen):
    """Displays a confirmation dialog to exit the game."""
    # Initialize font and colors
    custom_font = "assets/fonts/sg.ttf"
    font = pygame.font.Font(custom_font, 48)
    dialog_color = (50, 50, 50)  # Dark gray for dialog box
    text_color = (255, 255, 255)  # White text
    button_color = (200, 200, 200)  # Gray buttons
    selected_color = (255, 255, 0)  # Highlighted button color

    # Dialog dimensions
    dialog_width, dialog_height = 600, 200
    dialog_rect = pygame.Rect(
        (screen.get_width() - dialog_width) // 2,
        (screen.get_height() - dialog_height) // 2,
        dialog_width,
        dialog_height,
    )

    # Dialog options
    options = ["Yes", "No"]
    selected_option = 0

    # Dialog loop
    dialog_running = True
    while dialog_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Exit the app immediately
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_RIGHT:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected_option] == "Yes":
                        pygame.quit()
                        exit()  # Exit the app when "Yes" is selected
                    elif options[selected_option] == "No":
                        return False  # Close dialog and resume the game

        # Draw dialog background
        pygame.draw.rect(screen, dialog_color, dialog_rect)
        pygame.draw.rect(screen, text_color, dialog_rect, 2)  # Border

        # Draw dialog text
        dialog_text = font.render("Exit the game?", True, text_color)
        dialog_text_rect = dialog_text.get_rect(
            center=(dialog_rect.centerx, dialog_rect.y + 50)
        )
        screen.blit(dialog_text, dialog_text_rect)

        # Draw options
        for i, option in enumerate(options):
            color = selected_color if i == selected_option else button_color
            text = font.render(option, True, color)
            text_rect = text.get_rect(
                center=(
                    dialog_rect.x + 200 + i * 200,
                    dialog_rect.y + dialog_height - 50,
                )
            )
            screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()
