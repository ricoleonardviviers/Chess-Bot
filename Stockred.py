from stockfish import Stockfish

class bot:
    def __init__(self):
        self.stockfish = Stockfish(path="stockfish.exe")
        self.set_up_board()

    def set_up_board(self):
        self.stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def board_visual(self):
        return self.stockfish.get_board_visual()
