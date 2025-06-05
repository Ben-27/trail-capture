# game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 5
PLAYER_SPEED = 20 / TILE_SIZE # original TILE_SIZE = 10, PLAYER_SPEED = 2

DIRECTIONS = {
    'NORTH': (0, -1),
    'SOUTH': (0, 1),
    'EAST': (1, 0),
    'WEST': (-1, 0)
}

# colors
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

COLORS = {'player': 0, 'owned': 1, 'trail': 2}

PLAYER_COLORS = {
    'reds': [(183, 28, 28), (239, 83, 80), (211, 47, 47)],
    'purples': [(74, 20, 140), (186, 104, 200), (142, 36, 170)],
    'blues': [(26, 35, 126), (92, 107, 192), (57, 73, 171)],
    'greens': [(27, 94, 32), (102, 187, 106), (67, 160, 71)],
    'oranges': [(230, 81, 0), (255, 183, 77), (251, 140, 0)]
}