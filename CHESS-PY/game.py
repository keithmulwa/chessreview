
from move import MoveLogic
from ai_logic import AILogic
from board import Board
from model import Model

class Game:
    
    def __init__(self):

        print("Two kingdoms. One board. Infinite possibilities. Your move, Grandmaster.")
        self.player_white = input("Enter name for White: ")
        self.player_black = "AI"
        self.board = Board("white")
        self.board.display_pieces()
        self.move_logic = MoveLogic(self.board)
        self.ai = AILogic("black")
        self.current_turn = "white"
        self.is_game_over = False
        self.model = Model()
        if self.model.conn:
            game_id = self.model.start_game(self.player_white, self.player_black)
            if game_id:
                print(f"Game started successfully with ID: {game_id}")
            else:
                print("Failed to start game in database")
        else:
            print("No database connection available")

    def switch_turn(self):

        if self.current_turn == "white":
            self.current_turn = "black"
            print("Turn switched: It is now Black's move.")
        elif self.current_turn == "black":
            self.current_turn = "white"
            print("Turn switched: It is now White's move.")
        else:           
            return f"Invalid turn value: {self.current_turn}"

    def get_player_name(self):

        if self.current_turn == "white":
            player_name = self.player_white
            print(f"It is currently White's turn. Player: {player_name}")
        elif self.current_turn == "black":
            player_name = self.player_black
            print(f"It is currently Black's turn. Player: {player_name}")
        else:
            return f"Unexpected value for current_turn: {self.current_turn}"

        return player_name

    def input_to_board_coords(self, input_str):

        parts = input_str.split(",")

        if len(parts) != 2:
            print(f"Invalid input format: expected 2 values got {len(parts)}")
            return None
        
        for part in parts:
            if not part.strip().isdigit():
                print(f"Invalid input: '{part}' is not a number.")
                return None
        
        x = int(parts[0].strip()) 
        y = int(parts[1].strip()) 
        
        print(f"User input: horizontal = {x}, vertical = {y}")

        if x < 1 or x > 8:
            print(f"Invalid horizontal_choice: {x} is out of bounds. Must be between 1 and 8.")
            return None
        if y < 1 or y > 8:
            print(f"Invalid vertical_choice: {y} is out of bounds. Must be between 1 and 8.")
            return None
        

        board_x = x - 1
        board_y = 8 - y
        
        print(f"Board coordinates: x = {board_x}, y = {board_y}")
        return (board_x, board_y)

    def board_coords_to_display(self, board_x, board_y):
        display_x = board_x + 1
        display_y = 8 - board_y
        return f"{display_x},{display_y}"

    def play(self):

        while not self.is_game_over:
            self.board.display_board()
            print(f"\n{self.get_player_name()} ({self.current_turn}) to move.")

            if self.current_turn == "black":
                # AI move
                piece, move = self.ai.choose_move(self.board)
                if piece and move:
                    from_pos = (piece.x, piece.y)
                    moved = self.move_logic.execute_move(piece, move)
                    if moved:
                        move_str = self.board_coords_to_display(*move)
                        print(f"AI moved {piece.symbol} to {move_str}")
                        
                        # Log AI move to database
                        if self.model.conn:
                            move_data = {
                                'piece': piece.symbol,
                                'from': from_pos,
                                'to': move
                            }
                            self.model.log_move(move_data, self.current_turn)
                        
                        self.switch_turn()
                    else:
                        print("AI move failed.")
                else:
                    print("AI has no valid moves.")
                continue

            # Human move
            from_input = input("Select piece to move (format: x,y where x=horizontal digits, y=vertical digits): ")
            from_coords = self.input_to_board_coords(from_input)
            if not from_coords:
                print("Invalid input format. Use numbers like '4,2' (x 4, y 2).")
                continue

            from_x, from_y = from_coords
            
            if not self.board.is_inbounds(from_x, from_y):
                print("Position out of bounds.")
                continue
                
            piece = self.board.board[from_y][from_x]
            if not piece:
                print("No piece at that position.")
                continue
            if piece._color != self.current_turn:
                print("That's not your piece.")
                continue

            valid_moves = piece.valid_moves(self.board)
            if not valid_moves:
                print("This piece has no valid moves.")
                continue
                
            print("Valid moves:", [self.board_coords_to_display(x, y) for x, y in valid_moves])

            to_input = input("Enter destination (format: x,y): ")
            to_coords = self.input_to_board_coords(to_input)
            if not to_coords:
                print("Invalid input format.")
                continue

            to_x, to_y = to_coords
            
            # Check if the move is valid
            if (to_x, to_y) not in valid_moves:
                print("Invalid move. Try again.")
                continue

            # Execute the move
            moved = piece.move(to_x, to_y, self.board)
            if moved:
                move_str = self.board_coords_to_display(to_x, to_y)
                print(f"{self.get_player_name()} moved {piece.symbol} to {move_str}")
                
                # Log move to database
                if self.model.conn:
                    move_data = {
                        'piece': piece.symbol,
                        'from': (from_x, from_y),
                        'to': (to_x, to_y)
                    }
                    self.model.log_move(move_data, self.current_turn)
                
                self.switch_turn()  
            else:
                print("Move failed.")
        
game1 = Game()
game1.play()
