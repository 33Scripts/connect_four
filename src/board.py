from utils import clear_screen
from time import sleep


class Board:
    """Represents a Connect Four game board.
    
    The board consists of rows and columns where players can drop their pieces.
    Each cell can be empty or contain a colored player token.
    
    Attributes:
        rows (int): Number of rows in the board.
        columns (int): Number of columns in the board.
        empty (str): Character representing an empty cell.
        token (str): Character used to display player tokens.
        board (list): 2D list representing the game board state.
    """
    
    def __init__(self, rows, columns):
        """Initialize a new game board.
        
        Args:
            rows (int): Number of rows in the board.
            columns (int): Number of columns in the board.
        """
        self.rows = rows
        self.columns = columns
        self.empty = '.'
        self.token = 'O'
        self.board = [[self.empty for _ in range(columns)] for _ in range(rows)]
    
    def drop_piece(self, col, color):
        """Drop a colored piece in the specified column with animation.
        
        Args:
            col (int): The column index to drop the piece in.
            color (str): The color code for the player's piece.
        
        Returns:
            bool: True if the piece was successfully dropped, False otherwise.
        """
        if self.is_valid_move(col):
            # Determine the target row where the piece will settle
            target_row = None
            for row in range(self.rows - 1, -1, -1):
                if self.board[row][col] == self.empty:
                    target_row = row
                    break
                    
            if target_row is None:
                return False

            # Animate the piece falling from the top to the target row
            for row in range(target_row + 1):
                if row > 0:
                    # Clear the previous position
                    self.board[row - 1][col] = self.empty
                # Place piece at the current row
                self.board[row][col] = color
                clear_screen()
                self.print_board()
                sleep(0.1)
            
            return True
        return False
    
    def is_valid_move(self, col):
        """Check if a move is valid.

        A valid move means the selected column has at least one empty cell at the top.

        Args:
            col (int): The column index to check.
        
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the column is not full (top cell is empty)
        return self.board[0][col] == self.empty
    
    def check_winner(self):
        """Check if there is a winner on the board.
        
        Checks for four consecutive same-colored pieces horizontally,
        vertically, or diagonally across the board.
        
        Returns:
            str: The color code of the winning token if found, None otherwise.
        """
        for row in range(self.rows):
            for col in range(self.columns):
                token = self.board[row][col]
                if token != self.empty:
                    # Check for a horizontal win (right)
                    if col <= self.columns - 4:
                        if (self.board[row][col+1] == token and 
                            self.board[row][col+2] == token and 
                            self.board[row][col+3] == token):
                            return token

                    # Check for a vertical win (down)
                    if row <= self.rows - 4:
                        if (self.board[row+1][col] == token and 
                            self.board[row+2][col] == token and 
                            self.board[row+3][col] == token):
                            return token

                    # Check for a downward diagonal win (right-down)
                    if row <= self.rows - 4 and col <= self.columns - 4:
                        if (self.board[row+1][col+1] == token and 
                            self.board[row+2][col+2] == token and 
                            self.board[row+3][col+3] == token):
                            return token

                    # Check for an upward diagonal win (right-up)
                    if row >= 3 and col <= self.columns - 4:
                        if (self.board[row-1][col+1] == token and 
                            self.board[row-2][col+2] == token and 
                            self.board[row-3][col+3] == token):
                            return token
        
        return None

    def is_full(self):
        """Check if the board is completely filled.
        
        Returns:
            bool: True if the board is full, False otherwise.
        """
        # Check if any cell is empty
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == self.empty:
                    return False
        return True

    def print_board(self):
        """Display the current state of the board to the console.
        
        Empty cells are shown as dots, and player pieces are shown
        with their respective colors.
        """
        for row in self.board:
            for cell in row:
                if cell == self.empty:
                    print(cell, end='  ')
                else:
                    # Print colored player token
                    print(f'{cell}{self.token}', end='  ')
            print()
            
        # Print column numbers for user reference
        print('  '.join(str(i+1) for i in range(self.columns)))

    def clear_board(self):
        """Reset the board to empty state.
        
        All cells are set back to the empty value.
        """
        self.board = [[self.empty for _ in range(self.columns)] for _ in range(self.rows)]

