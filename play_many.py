import chess

from dumbchess.agents import MinimaxAgent, RandomAgent
from dumbchess.game import Game

bots = (RandomAgent(chess.BLACK), MinimaxAgent(chess.WHITE, depth=3))

for i in range(15):
    game = Game(*bots)
    result = game.play(print_board=False)
    print(result)
