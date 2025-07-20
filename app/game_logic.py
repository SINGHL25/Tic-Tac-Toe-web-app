class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            if self.check_winner(self.current_player):
                return f"{self.current_player} wins"
            self.current_player = "O" if self.current_player == "X" else "X"
        return None

    def check_winner(self, player):
        win_pos = [(0,1,2), (3,4,5), (6,7,8), 
                   (0,3,6), (1,4,7), (2,5,8), 
                   (0,4,8), (2,4,6)]
        return any(all(self.board[pos] == player for pos in line) for line in win_pos)

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"

