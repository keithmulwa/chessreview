from chess.board import Board
from chess.pawn import Pawn
from chess.rook import Rook
from chess.bishop import Bishop
from chess.queen import Queen
from chess.knight import Knight
from chess.king import King

class GameManager:
    def board_to_json(self, board):
        pieces = []
        for y in range(8):
            for x in range(8):
                piece = board.board[y][x]
                if piece:
                    pieces.append({
                        'type': piece.__class__.__name__,
                        'color': piece._color,
                        'x': x,
                        'y': y
                    })
        return {'pieces': pieces}

    def json_to_board(self, data):
        board = Board('white')
        for piece_data in data['pieces']:
            piece_type = piece_data['type']
            color = piece_data['color']
            x = piece_data['x']
            y = piece_data['y']
            if piece_type == 'Pawn':
                piece = Pawn(color, x, y)
            elif piece_type == 'Rook':
                piece = Rook(color, x, y)
            elif piece_type == 'Bishop':
                piece = Bishop(color, x, y)
            elif piece_type == 'Queen':
                piece = Queen(color, x, y)
            elif piece_type == 'Knight':
                piece = Knight(color, x, y)
            elif piece_type == 'King':
                piece = King(color, x, y)
            board.board[y][x] = piece
        return board
