from game import*
from player import*


pygame.init()

if __name__ == "__main__":
    game = Game()
    game.run()
    main()

pygame.quit()
sys.exit()