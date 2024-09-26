import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import AsteroidField 
import sys




def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(x, y)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update the player 
        for item in updateable:
            item.update(dt)

        for item in asteroids:
            if player.is_colliding(item):
                print("Game Over!")
                sys.exit()


        # Fill the screen with black
        color = pygame.Color('black')
        screen.fill(color)

        # Draw the player
        for item in drawable:
            item.draw(screen)

        #Refresh the display
        pygame.display.flip()
      
        # Control the frame rate
        dt = clock.tick(60) / 1000











if __name__ == "__main__":
    main()
