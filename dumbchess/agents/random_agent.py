import random

import chess

from .agent import Agent


class RandomAgent(Agent):
    def pick_move(self, board: chess.Board) -> chess.Move:
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)
