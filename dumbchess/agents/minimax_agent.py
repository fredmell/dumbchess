import chess

from .agent import Agent

piece_values = {
    chess.PAWN: 1.0,
    chess.KNIGHT: 3.0,
    chess.BISHOP: 3.0,
    chess.ROOK: 5.0,
    chess.QUEEN: 9.0,
    chess.KING: 999.0,
}


class MinimaxAgent(Agent):
    def __init__(self, color: chess.Color, depth: int = 3):
        super().__init__(color)
        self.depth = depth

    def evaluate_board(self, board: chess.Board) -> float:
        white_value = sum(
            piece_values[piece_type]
            * len(board.pieces(piece_type, chess.WHITE))
            for piece_type in piece_values
        )

        black_value = sum(
            piece_values[piece_type]
            * len(board.pieces(piece_type, chess.BLACK))
            for piece_type in piece_values
        )

        return white_value - black_value

    def minimax(
        self,
        board: chess.Board,
        depth: int,
        α: float,
        β: float,
        maximizing: bool,
    ) -> float:
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        legal_moves = board.legal_moves

        if maximizing:
            value = -float("inf")
            for move in legal_moves:
                board.push(move)
                value = max(value, self.minimax(board, depth - 1, α, β, False))
                board.pop()
                α = max(α, value)
                if α >= β:
                    break
            return value

        else:  # Minimizing player
            value = float("inf")
            for move in legal_moves:
                board.push(move)
                value = min(value, self.minimax(board, depth - 1, α, β, True))
                board.pop()
                β = min(β, value)
                if β <= α:
                    break
            return value

    def pick_move(self, board: chess.Board) -> chess.Move:
        possible_moves = list(board.legal_moves)
        values = []

        for move in possible_moves:
            board.push(move)
            value = self.minimax(
                board,
                self.depth - 1,
                -float("inf"),
                float("inf"),
                bool(self.color),
            )
            board.pop()
            values.append((move, value))

        if self.color == chess.WHITE:
            best_move = max(values, key=lambda x: x[1])[0]
        else:
            best_move = min(values, key=lambda x: x[1])[0]

        return best_move
