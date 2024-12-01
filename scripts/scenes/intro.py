import pygame
from scripts.addons.exit_screen import show_exit_dialog

def run_intro(screen):
    # Initialize font
    custom_font_path = "assets/fonts/sg.ttf"
    font = pygame.font.Font(custom_font_path, 36)  # Use custom font with size 36
    
    # Load background and character images
    background = pygame.image.load("assets/backgrounds/testb.png")
    character = pygame.image.load("assets/characters/moomsekiranun/concept1.png")

    # Scale images to fit the screen
    background = pygame.transform.scale(background, screen.get_size())

    # Example dialogues
    dialogues = [
        "Press Space to go to the next dialogue",
        "Hello there!",
        "This is Moom Sekiranun. The Main Character of the game.",
        "Concept art phase.",
        "End of Dialogues."
    ]

    # Dialogue index
    dialogue_index = 0

    # Game loop for the intro
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or pygame.K_RETURN:  # Check if the spacebar is pressed
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        running = False  # Exit the loop when dialogues are over
                elif event.key == pygame.K_ESCAPE:  # Check for ESC key
                    if show_exit_dialog(screen):
                        running = False  # Exit if user confirms to quit
        
        # Draw background
        screen.blit(background, (0, 0))

        # Draw character in the middle of the screen
        character_x = (screen.get_width() - character.get_width()) // 2
        character_y = (screen.get_height() - character.get_height()) // 2
        screen.blit(character, (character_x, character_y))

        # Render and display current dialogue text
        if dialogue_index < len(dialogues):
            text = font.render(dialogues[dialogue_index], True, (255, 255, 255))
            text_x = (screen.get_width() - text.get_width()) // 2  # Center horizontally
            text_y = screen.get_height() - text.get_height() - 50  # Position near the bottom
            screen.blit(text, (text_x, text_y))
        
        # Update the display
        pygame.display.flip()
