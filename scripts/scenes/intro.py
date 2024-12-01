import pygame
from scripts.addons.scene_exit_screen import show_exit_dialog


def run_intro(screen):

    # Initialize Pygame mixer for sound
    pygame.mixer.init()

    # Load and play background music
    music_path = "assets/audio/music/sekiranungraffitikaraoke.mp3"
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(loops=-1, start=0.0)  # Loops indefinitely

    # Initialize font
    custom_font_path = "assets/fonts/sg.ttf"
    font = pygame.font.Font(custom_font_path, 24)  # Use custom font with size 24
    
    # Load background and character images
    background = pygame.image.load("assets/backgrounds/testb.png")
    character = pygame.image.load("assets/characters/moomsekiranun/concept1.png")

    # Get the original dimensions of the image
    original_width, original_height = character.get_width(), character.get_height()
    scale_factor = 0.5 
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    character = pygame.transform.scale(character, (new_width, new_height))

    # Scale images to fit the screen
    background = pygame.transform.scale(background, screen.get_size())

    # Example dialogues
    dialogues = [
        "Press Space/Enter...",
        "Hello there!",
        "Or... Hello World.",
        "This is Moom Sekiranun. The Main Character of the game. How do I don't know that, I guess I'm breaking the 4th wall.",
        "Oh whatever...",
        "Cry me a river.",
        "Well I like daydreaming.",
        "I'm a 2nd year University student at [...]. I'm planning to major in[...] and [...].",
        "I have dissociate identity disorder",
        "So... If I'm acting strange, I would suggest getting the heck out.",
        "I live in an apartment downtown. There's 3 elevators that I can take to the 9th floor.",
        "Sometimes it's annoying when the people below me smoke.",
        "Anyways. I'm still in development so my interests/identity could change.",
        "Momo out.",
        "We're concept art phase.",
        "Game coming out in estimated. 2030.",
        "Bye."
    ]

    # Dialogue index
    dialogue_index = 0

    # Character's name
    character_name = "Moom Sekiranun"

    # Game loop for the intro
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_a:  # Check if the spacebar is pressed
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

        # Create a black box behind the gradient text box
        text_box_height = 150  # Height of the text box
        text_box_width = screen.get_width()
        
        # Create a surface for the black box
        text_box_surface = pygame.Surface((text_box_width, text_box_height))
        text_box_surface.fill((0, 0, 0))  # Black background

        # Blit the black box surface onto the screen
        screen.blit(text_box_surface, (0, screen.get_height() - text_box_height))

        # Create a semi-transparent, lighter gray gradient text box on top of the black box
        gradient_box_surface = pygame.Surface((text_box_width, text_box_height), pygame.SRCALPHA)
        gradient_box_surface.fill((200, 200, 200, 50))  # Light gray with some transparency

        # Blit the gradient text box surface on top of the black box
        screen.blit(gradient_box_surface, (0, screen.get_height() - text_box_height))

        # Render and display character's name at the top of the text box
        name_text = font.render(f"{character_name}: ", True, (255, 255, 255))
        name_x = 20  # Padding from the left edge
        name_y = screen.get_height() - text_box_height + 20  # Padding from the top of the text box
        screen.blit(name_text, (name_x, name_y))

        # Render and display current dialogue text, below the character's name
        if dialogue_index < len(dialogues):
            dialogue_text = dialogues[dialogue_index]
            # Wrap text to fit within the width of the text box
            wrapped_text = wrap_text(dialogue_text, font, text_box_width - 40)  # 40 is for padding
            dialogue_y = name_y + name_text.get_height() + 20  # Space between name and dialogue text

            # Draw each line of wrapped text with indentation
            for line in wrapped_text:
                line_text = font.render(f"    {line}", True, (255, 255, 255))  # Indentation for dialogue
                screen.blit(line_text, (name_x, dialogue_y))
                dialogue_y += line_text.get_height() + 5  # Add some space between lines

        # Update the display
        pygame.display.flip()

    # Stop the music when exiting
    pygame.mixer.music.stop()


def wrap_text(text, font, max_width):
    """
    Wraps the input text to fit within the specified width.
    Adds some padding to avoid touching the edge of the screen.
    """
    words = text.split(' ')
    lines = []
    current_line = ""

    # Reduce the max width to add some padding
    max_width -= 40  # Leave a 20px margin on both sides

    for word in words:
        # Check the width of the current line with the new word
        test_line = f"{current_line} {word}".strip()
        test_width = font.size(test_line)[0]

        if test_width <= max_width:
            # Add the word to the current line
            current_line = test_line
        else:
            # Start a new line if the current line is too long
            lines.append(current_line)
            current_line = word

    # Add the last line
    if current_line:
        lines.append(current_line)

    return lines
