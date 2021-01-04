import argparse

import chess

from dumbchess.agents import MinimaxAgent, PlayerAgent, RandomAgent
from dumbchess.game import Game

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--color",
        choices=("w", "b"),
        default="w",
        help="Color to play, defaults to w",
    )
    args = parser.parse_args()

    if args.color == "w":
        player_color = chess.WHITE
    else:
        player_color = chess.BLACK

    player = PlayerAgent(player_color)
    bot = MinimaxAgent(not player_color, depth=4)

    game = Game(player, bot)
    result = game.play(print_board=True)

    print(game.board)
    print(result)
