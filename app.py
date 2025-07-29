from phrasehunter.game import Game

if __name__ == '__main__':
    playing = True
    while playing:
        game = Game()
        playing = game.start()