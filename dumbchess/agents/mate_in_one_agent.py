import random

import chess

from .agent import Agent


class MateInOneAgent(Agent):
    def pick_move(self, b: chess.Board) -> chess.Move:
        board = b.copy()
        legal_moves = list(board.legal_moves)

        mate = None
        for legal_move in legal_moves:
            # Make the move
            board.push(legal_move)

            # Check for mate
            if board.is_checkmate():
                mate = legal_move
                break

            # Restore board position
            board.pop()

        if mate:
            move = mate
        else:
            move = random.choice(legal_moves)
        return move
