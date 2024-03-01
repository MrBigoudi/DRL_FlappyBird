from game import Game

def main ():
    newGame = Game()
    newGame.init("flappy bird DRL")
    newGame.run()
    return 0


if __name__=="__main__":
    main()