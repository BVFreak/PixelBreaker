import pygame

def get_font(size: int):
    """Gets font.

    Args:
        size (int): how big the font is.

    Returns:
       pygame.font: font loaded
    """
    return pygame.font.Font("assets/fonts/font.ttf", int(size))