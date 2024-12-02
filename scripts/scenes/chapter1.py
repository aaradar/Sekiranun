import pygame

def chapter1(screen):
     # Load and play background music
    music_path = "assets/audio/music/sekiranungraffitikaraoke.mp3"
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(loops=-1, start=0.0)  # Loops indefinitely

    # Initialize font
    custom_font_path = "assets/fonts/sg.ttf"
    font = pygame.font.Font(custom_font_path, 24)  # Use custom font with size 24
    
    # Load background and character images
    background = pygame.image.load("assets/backgrounds/testb.png")