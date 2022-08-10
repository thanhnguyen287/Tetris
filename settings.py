import pygame
sq_size = 32
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
    (128,128,128)
]

def draw_text(screen, text, size, color, pos):
    # create a Font object from the system fonts
    # SysFont(name, size, bold=False, italic=False)

    # font = pygame.font.SysFont(None, size)

    font = pygame.font.SysFont('Times New Roman', size)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)

    screen.blit(text_surface, text_rect)
