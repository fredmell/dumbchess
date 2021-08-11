import abc

import chess


class Agent(abc.ABC):
    def __init__(self, color: chess.Color):
        self.color = color

    @abc.abstractmethod
    def pick_move(board: chess.Board) -> chess.Move:
        """Given the state of the board, choose the move to play"""
