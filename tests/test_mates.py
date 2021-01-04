import unittest

import chess

import dumbchess


class MinimaxMates(unittest.TestCase):
    def test_rook_mate_in_one(self):
        board = chess.Board("8/7k/8/8/8/6R1/1K6/R7 w - - 0 1")
        agent = dumbchess.agents.MinimaxAgent(chess.WHITE, depth=2)
        move = agent.pick_move(board)
        self.assertEqual(move, chess.Move.from_uci("a1h1"))
