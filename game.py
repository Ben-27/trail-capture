import random

from config import *
from utils import *

class Player:
    def __init__(self, x, y, colors, controls, name):
        '''
        Params:
            x: int, x-coordinate of position
            y: int, y-coordinate of position
            colors: dict[attr: tuple of RGB]
            controls: dict[direction: key]
        '''
        self.x = x
        self.y = y
        self.colors = colors
        self.controls = controls
        self.name = name
        self.game_over = False

        self.direction = 'NORTH'
        self.trail = []
        
        # create initial owned region
        self.owned_tiles = set()
        sx, sy = self.x // TILE_SIZE, self.y // TILE_SIZE
        self.owned_tiles.add((sx, sy))

        delta = int(PLAYER_SPEED)
        for dx in range(-delta, delta+1):
            for dy in range(-delta, delta+1):
                self.owned_tiles.add((sx + dx, sy + dy))

    def reset(self):
        '''
        Resets player to a random position and resets attributes.
        '''
        if self.owned_tiles:
            self.x, self.y = [TILE_SIZE*i for i in random.choice(list(self.owned_tiles))]
            self.trail.clear()
            self.direction = random.choice(list(DIRECTIONS.keys()))
        # GAME OVER
        else:
            self.game_over = True

    def handle_input(self, keys):
        '''
        Sets direction based on input.
        '''
        for d in DIRECTIONS:
            if keys[self.controls[d]]:
                self.direction = d

    def move(self):
        # player location
        dx, dy = tuple(x * PLAYER_SPEED for x in DIRECTIONS[self.direction])

        self.x += dx
        self.y += dy

        # border collision detection
        self.x = max(0, min(self.x, SCREEN_WIDTH - TILE_SIZE))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - TILE_SIZE))

        # add position to trail if it is not in owned tiles
        pos = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        if pos not in self.owned_tiles:
            self.trail.append(pos)

    def get_head_pos(self):
        return (self.x // TILE_SIZE, self.y // TILE_SIZE)
    
    def update_ownership(self):
        '''
        Add trail to owned tiles
        '''
        for pos in self.trail:
            self.owned_tiles.add(pos)
        self.trail.clear()

        # fill region
        width_tiles = SCREEN_WIDTH // TILE_SIZE
        height_tiles = SCREEN_HEIGHT // TILE_SIZE
        blocked = set(self.owned_tiles)
        reachable = flood_fill_exterior(width_tiles, height_tiles, blocked)
        # enclosed are all_tiles that are not already owned or on the exterior
        all_tiles = {(x, y) for x in range(width_tiles) for y in range(height_tiles)}
        enclosed = all_tiles - reachable - self.owned_tiles

        self.owned_tiles.update(enclosed)