# Asteroids Game
# Made by: Nicholas O'Brien
# Date: Oct 2026
# With help from: Boot.dev

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    dt: float = 0.0

    #Initialises the pygame
    pygame.init()
    # New object created "Player"
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # New clock variable created
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Our game simply creates a black screen for now
        screen.fill("black")

        #Render the player after filling the screen black
        player.draw(screen)

        #Update the player frame if a or d are pressed (rotate)
        player.update(dt)

        #Refreshes the screen (i think)
        pygame.display.flip()

        # a delta time variable unused. Perhaps just using processing power
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
