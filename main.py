import pygame
import sys

from game import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    players = [
        Player(
            100, 100, PLAYER_COLORS['reds'],
            {'NORTH': pygame.K_w, 'EAST': pygame.K_d, 'SOUTH': pygame.K_s, 'WEST': pygame.K_a},
            'Player 1'
        ),
        Player(
            700, 500, PLAYER_COLORS['blues'],
            {'NORTH': pygame.K_UP, 'EAST': pygame.K_RIGHT, 'SOUTH': pygame.K_DOWN, 'WEST': pygame.K_LEFT},
            'Player 2'
        )
    ]

    game_map = {}

    running = True
    while running:
        screen.fill(GRAY)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # handle movement and collisions
        for player in players:
            player.handle_input(keys)
            player.move()
            head = player.get_head_pos()

            # close trail into region
            if head in player.owned_tiles:
                player.update_ownership()
                # overtake other's ownership
                for other in players:
                    if other != player:
                        other.owned_tiles = other.owned_tiles - player.owned_tiles
                    
            # check for collision
            for other in players:
                # player hits other's tail -> other resets
                if other != player and head in other.trail:
                    other.reset()
                # same player: cannot collide with own tail
                # player that hits wall without turning immediately will reset
                elif head in other.trail[:-(TILE_SIZE + 1)]: # ignore last tile + 1 of trail
                    player.reset()          

        # draw owned regions on background
        for player in players:
            for tile in player.owned_tiles:
                pygame.draw.rect(screen, player.colors[COLORS['owned']], (*[i * TILE_SIZE for i in tile], TILE_SIZE, TILE_SIZE))
        
        # draw trails above owned regions
        for player in players:
            for tile in player.trail:
                pygame.draw.rect(screen, player.colors[COLORS['trail']], (*[i * TILE_SIZE for i in tile], TILE_SIZE, TILE_SIZE))

        # draw players on final layer
        for player in players:
            pygame.draw.rect(screen, player.colors[COLORS['player']], (player.x, player.y, TILE_SIZE, TILE_SIZE))

        # check if game is over
        for player in players:
            if player.game_over:
                running = False

        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
            