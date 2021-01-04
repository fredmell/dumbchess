import chess

from dumbchess.agents.agent import Agent


class Game:
    def __init__(self, player1: Agent, player2: Agent):
        assert player1.color != player2.color
        self.player1 = player1
        self.player2 = player2

        self.board = chess.Board()

    def play(self, print_board: bool = False) -> str:
        if print_board:
            print(self.board)

        while not self.board.is_game_over():
            if self.board.turn == self.player1.color:
                move = self.player1.pick_move(self.board)
            else:
                move = self.player2.pick_move(self.board)

            self.board.push(move)
            if print_board:
                print(self.board)

        return self.board.result()
