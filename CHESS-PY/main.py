from chess.board import Board

def main():
    # Initialize the chess board
    board = Board("white")  # Perspective from white's side

    # Set up the initial pieces
    board.display_pieces()

    # Display the board
    board.display_board()

    print("Welcome to Chess CLI! This is a simple display of the starting board.")
    print("You can expand this to handle moves, AI, etc.")

if __name__ == "__main__":
    main()
