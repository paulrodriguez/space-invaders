# Libraries
import sys,pygame
from settings import Settings
from spaceship import Spaceship

game_settings = Settings()
game_ship = Spaceship()



def run_game():
    pygame.init();
    screen = game_settings.getScreen()
    pygame.display.set_caption("Space Invaders")
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))

        game_ship.move()

        game_ship.draw(screen)
        pygame.display.flip()
        clock.tick(120)
    #pygame.quit()
    #sys.exit()
run_game()
