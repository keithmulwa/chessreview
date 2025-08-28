from pawn import Pawn
from rook import Rook
from bishop import Bishop
from queen import Queen
from knight import Knight
from king import King

class Board:

    black_pieces = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]  # Black major pieces
    white_pieces = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]  # White major pieces
    black_pawn = "♟"
    white_pawn = "♙"

    def __init__(self,color):
        
        self.board = []
        self._color = color

        for i in range(8):
            y = []
            for j in range (8):
                y.append(None)
            self.board.append(y)

    def display_board(self):
        print("       1         2          3          4          5          6           7         8")
        print("  ---------" * 8)
    
        for i in range(8):
            y=self.board[i]
            display_row = []
        
            for square in y:
                if square is None:
                    display_row.append("|        |")
                elif isinstance(square, Pawn):
                    display_row.append(f"|   {square.symbol}    |")
                elif isinstance(square, (Rook, Bishop,Knight,Queen,King)):
                        
                        display_row.append(f"|   {square.symbol}    |")    
                else:
                    display_row.append(square)
        
            print(f"{8-i}:{' '.join(display_row)}")
            print("  ---------" * 8)
    
        print("       1         2          3          4          5          6           7         8")


    def display_pieces(self):
        
        # Black pieces (top of board - row 0)
        self.board[0][0] = Rook("black", 0, 0)
        self.board[0][1] = Knight("black",1,0)  
        self.board[0][2] = Bishop("black", 2, 0)
        self.board[0][3] = Queen ("black",3,0) 
        self.board[0][4] = King("black",4,0)
        self.board[0][5] = Bishop("black", 5, 0)
        self.board[0][6] = Knight("black",6,0)
        self.board[0][7] = Rook("black", 7, 0)
        
        # Black pawns (row 1)
        for i in range(8):
            self.board[1][i] = Pawn("black", i, 1)
        
        # White pawns (row 6)
        for i in range(8):
            self.board[6][i] =Pawn("white", i, 6)
            
        # White pieces (bottom of board - row 7)
        self.board[7][0] = Rook("white", 0, 7)
        self.board[7][1] = Knight("white",1,7)  
        self.board[7][2] = Bishop("white", 2, 7)
        self.board[7][3] = Queen( "white",3,7)  
        self.board[7][4] = King("white",4,7)  
        self.board[7][5] = Bishop("white", 5, 7)
        self.board[7][6] = Knight("white",6,7)  
        self.board[7][7] = Rook("white", 7, 7)

    def is_inbounds(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    def is_square_empty(self, x, y):
        return self.is_inbounds(x, y) and self.board[y][x] is None

    def is_enemy_piece(self, color, x, y):
        if not self.is_inbounds(x, y) or self.is_square_empty(x, y):
            return False
        piece = self.board[y][x]
        
        if hasattr(piece, '_color'):
            return piece._color != color
        return False

    def get_piece(self, x, y):
        board_x = x - 1  
        board_y = y - 1
        
        if not self.is_inbounds(board_x, board_y):
            return None
        
        return self.board[board_y][board_x]


