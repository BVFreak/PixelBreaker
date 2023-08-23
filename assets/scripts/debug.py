from .font import get_font

def debug(screen, debug_value):
    DEBUG_TEXT = get_font(50).render(f"{debug_value}", True, "white").convert_alpha()
    DEBUG_RECT = DEBUG_TEXT.get_rect(center=(100, 100))
    screen.blit(DEBUG_TEXT, DEBUG_RECT)
