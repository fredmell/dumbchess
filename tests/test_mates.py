import unittest

import chess

from dumbchess.agents import MateInOneAgent


class MateInOneMates(unittest.TestCase):
    def test_rook_mate_in_one(self):
        board = chess.Board("8/7k/8/8/8/6R1/1K6/R7 w - - 0 1")
        agent = MateInOneAgent(chess.BLACK)
        move = agent.pick_move(board)
        self.assertEqual(move, chess.Move.from_uci("a1h1"))

    def test_knight_mate_in_one(self):
        board = chess.Board(
            "rnb1kb1r/pppp1p1p/1nN1p1p1/8/6N1/8/PPPPPPPP/q1BQKB1R w Kkq - 0 1"
        )
        agent = MateInOneAgent(chess.WHITE)
        move = agent.pick_move(board)
        self.assertEqual(move, chess.Move.from_uci("g4f6"))


class MateInTwoMates(unittest.TestCase):
    def test_rook_mate_in_two(self):
        board = chess.Board("7k/5ppp/5ppp/8/8/3K4/3R4/8 w - - 0 1")
        agent = MateInOneAgent(chess.WHITE)

        move = agent.pick_move(board)
        board.push(move)

        board.push(chess.Move.from_uci("h6h5"))

        move = agent.pick_move(board)
        board.push(move)

        self.assertTrue(board.is_checkmate())
