# utils/tic_tac_toe.py
class TicTacToe:
    def __init__(self):
        self.winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def check_winner(self, board):
        for pos in self.winning_positions:
            a, b, c = pos
            if board[a] and board[a] == board[b] == board[c]:
                return board[a]
        return None
