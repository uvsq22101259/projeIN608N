import pygame

WINDOW_SIZE = (1280, 720)
CELL_SIZE = WINDOW_SIZE[1]//9.6
GRID_LENGTH = 9

FONT_SIZE = WINDOW_SIZE[1]//16

RAYON = CELL_SIZE // 4

WHITE = (255, 255, 255)
VIDE = (101, 67, 32)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

back_image = pygame.image.load("assets/bg.png")
back_image = pygame.transform.scale(back_image, WINDOW_SIZE)
clock = pygame.time.Clock()
