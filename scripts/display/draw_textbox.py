import pygame

class DrawTextBox:
    def __init__(self, screen, font, character_name, dialogues, dialogue_index, text_box_height=150):
        """
        Initializes the DrawTextBox object and prepares the surfaces for rendering.

        :param screen: The pygame screen where the text box will be displayed.
        :param font: The pygame font object for rendering text.
        :param character_name: Name of the character to display.
        :param dialogues: List of dialogue strings.
        :param dialogue_index: Index of the current dialogue to display.
        :param text_box_height: Height of the text box.
        """
        self.screen = screen
        self.font = font
        self.character_name = character_name
        self.dialogues = dialogues
        self.dialogue_index = dialogue_index
        self.text_box_height = text_box_height
        self.text_box_width = screen.get_width()

    def display(self):
        """Renders the text box, character name, and dialogue onto the screen."""
        # Create a surface for the black box
        text_box_surface = pygame.Surface((self.text_box_width, self.text_box_height))
        text_box_surface.fill((0, 0, 0))  # Black background

        # Blit the black box surface onto the screen
        self.screen.blit(text_box_surface, (0, self.screen.get_height() - self.text_box_height))

        # Create a semi-transparent gradient text box on top of the black box
        gradient_box_surface = pygame.Surface((self.text_box_width, self.text_box_height), pygame.SRCALPHA)
        gradient_box_surface.fill((200, 200, 200, 50))  # Light gray with some transparency

        # Blit the gradient text box surface
        self.screen.blit(gradient_box_surface, (0, self.screen.get_height() - self.text_box_height))

        # Render and display character's name
        name_text = self.font.render(f"{self.character_name}:", True, (255, 255, 255))
        name_x = 20  # Padding from the left edge
        name_y = self.screen.get_height() - self.text_box_height + 20  # Padding from the top of the text box
        self.screen.blit(name_text, (name_x, name_y))

        # Render and display dialogue text
        if self.dialogue_index < len(self.dialogues):
            dialogue_text = self.dialogues[self.dialogue_index]
            # Wrap text to fit within the width of the text box
            wrapped_text = self.wrap_text(dialogue_text, self.font, self.text_box_width - 40)  # 40 is for padding
            dialogue_y = name_y + name_text.get_height() + 20  # Space between name and dialogue text

            # Draw each line of wrapped text with indentation
            for line in wrapped_text:
                line_text = self.font.render(f"    {line}", True, (255, 255, 255))  # Indentation for dialogue
                self.screen.blit(line_text, (name_x, dialogue_y))
                dialogue_y += line_text.get_height() + 5  # Add some space between lines

    @staticmethod
    def wrap_text(text, font, max_width):
        """
        Wraps the input text to fit within the specified width.
        Adds some padding to avoid touching the edge of the screen.
        
        :param text: The text to wrap.
        :param font: The pygame font object.
        :param max_width: Maximum width for the wrapped text.
        :return: A list of wrapped lines.
        """
        words = text.split(' ')
        lines = []
        current_line = ""

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
    
    def set_dialogue_index(self, index):
        """
        Sets the dialogue index to a specific value if it's within the valid range.

        :param index: The new dialogue index to set.
        :raises ValueError: If the index is out of bounds.
        """
        if 0 <= index < len(self.dialogues):
            self.dialogue_index = index
        else:
            raise ValueError(f"Index {index} is out of range. Valid range: 0 to {len(self.dialogues) - 1}")
