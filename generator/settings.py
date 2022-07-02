import pygame

BOARD_WIDTH = BOARD_HEIGHT = 720

NODE_WIDTH = NODE_HEIGHT = BOARD_WIDTH / 9
NUM_WIDTH = NUM_HEIGHT = NODE_WIDTH * 2

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GHOSTWHITE = (248, 248, 255)
DARKER_GHOSTWHITE = (220, 220, 255)
DARK_BLUE = (0, 0, 139)
RED = (255, 0, 0)

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

INPUTS = {pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9}
DIFFICULTY_INPUTS = {pygame.K_e, pygame.K_m, pygame.K_h, pygame.K_i}

DIFFICULTY = {"e": list(range(36, 47)),
              "m": list(range(32, 36)),
              "h": list(range(28, 32))}