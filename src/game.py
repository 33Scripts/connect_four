from board import Board
from utils import clear_screen


class Game:
    """Represents a Connect Four game.
    
    Controls the game flow, player turns, and win conditions for Connect Four.
    
    Attributes:
        board (Board): The game board.
        players (list): List containing the two players.
        current_player: The player whose turn it is.
        columns (int): Number of columns in the game board.
    """
    
    def __init__(self, player1, player2, rows, columns):
        """Initialize a new Connect Four game.
        
        Args:
            player1: The first player.
            player2: The second player.
            rows (int): Number of rows for the game board (between 4 and 10).
            columns (int): Number of columns for the game board (between 4 and 10).
        """
        # Ensure rows and columns are within valid range
        rows = min(max(rows, 4), 10)
        self.columns = min(max(columns, 4), 10)
        self.board = Board(rows, self.columns)
        self.players = [player1, player2]
        self.current_player = player1
    
    def switch_player(self):
        """Switch the current player to the other player."""
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play(self):
        """Start and control the game flow.
        
        Manages player turns, moves, and checks for win conditions.
        Allows for a new game after completion.
        """
        while True:
            clear_screen()
            self.board.print_board()
            
            try:
                # Get player's column choice (1-indexed for user, 0-indexed for code)
                col = int(input(f'{self.current_player.name}, enter a column (1-{self.columns}): ')) - 1
            except ValueError:
                input(f'Please enter an integer between 1 and {self.columns}. Press Enter to continue.')
                continue
                
            # Validate column choice
            if 0 <= col < self.columns:
                # Try to drop the piece
                if self.board.drop_piece(col, self.current_player.color):
                    # Check for win condition
                    if self.board.check_winner():
                        clear_screen()
                        self.board.print_board()
                        print(f'{self.current_player.name} wins!')
                        break
                    
                    # Check for tie
                    if self.board.is_full():
                        print("The board is full. It's a tie!")
                        break

                    # Switch to the other player's turn
                    self.switch_player()
                else:
                    input('Column is full. Try another column. Press Enter to continue.')
            else:
                input(f'Column out of range. Choose a column between 1 and {self.columns}. Press Enter to continue.')
                continue
        
        # Ask if players want to play again
        if input('Would you like to play again? Y/n: ').upper() == 'Y':
            self.board.clear_board()
            self.play()
