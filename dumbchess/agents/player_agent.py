import chess

from .agent import Agent


class PlayerAgent(Agent):
    def pick_move(self, board: chess.Board) -> chess.Move:
        move_is_legal = False
        move_input = input("Enter your desired move: ")
        try:
            move = chess.Move.from_uci(move_input)
            move_is_legal = move in board.legal_moves
        except ValueError:
            move_is_legal = False

        while not move_is_legal:
            move_input = input("Invalid or illegal move, please try again: ")
            try:
                move = chess.Move.from_uci(move_input)
                move_is_legal = move in board.legal_moves
            except ValueError:
                move_is_legal = False

        return move
