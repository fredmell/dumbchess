import abc

import chess


class Agent(abc.ABC):
    def __init__(self, color: chess.Color):
        self.color = color

    @abc.abstractmethod
    def pick_move(board: chess.Board) -> chess.Move:
        return
