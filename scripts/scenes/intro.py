import pygame
from scripts.addons.scene_exit_screen import show_exit_dialog
from scripts.helpers.user_input_handler import wait_user_input
from scripts.helpers.all_enums import UserInputOptions
from scripts.display.draw_background import display_background
from scripts.display.draw_character import Character
from scripts.display.draw_textbox import DrawTextBox

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

    character_file = "assets/characters/moomsekiranun/concept2.png"
    character = Character(character_file, scale_factor=0.5)

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

    text_box = DrawTextBox(screen, font, character_name, dialogues, dialogue_index)

    # Game loop for the intro
    running = True

    while running:
        # Event handling
        userInput = wait_user_input()

        if (userInput == UserInputOptions.NEXT):
            dialogue_index += 1
            text_box.set_dialogue_index(dialogue_index)
        if (userInput == UserInputOptions.QUIT):
            running = False
        if (userInput == UserInputOptions.ESC):
            if show_exit_dialog(screen):
                running = False
        if dialogue_index >= len(dialogues):
            running = False # Exit the loop when dialogues are over

        display_background(screen, "assets/backgrounds/apartmentlobby.png")

        character.displayCenter(screen)

        # Display the text box
        text_box.display()
        
        # Update the display
        pygame.display.flip()

    # Stop the music when exiting
    pygame.mixer.music.stop()