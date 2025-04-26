import pygame
from constants import *
from player import Player

def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x,y)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK_COLOR)

        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)

        '''
        player.update(dt)
        player.draw(screen)
        '''




        #end of loop reset
        pygame.display.flip()
        dt = clock.tick(60)/1000 #delay for 60 fps


if __name__ == "__main__":
    main()