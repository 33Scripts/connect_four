class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.empty = '.'
        self.token = 'O'
        self.board = [[self.empty for _ in range(columns)] for _ in range(rows)]
    
    def drop_piece(self, col, color):
        '''
        Drops a piece in the specified column.
        
        Args:
            col: The column to drop the piece in.
            token: The token to drop in the column.
        
        Returns:
            True if the piece was successfully dropped, False otherwise.
        '''

        if self.is_valid_move(col):
            # Iterate through the rows in the column from bottom to top and drop the piece in the first empty row.
            for row in range(self.rows - 1, -1, -1):
                if self.board[row][col] == self.empty:
                    self.board[row][col] = color
                    return True
        return False
    
    def is_valid_move(self, col):
        '''
        Checks if a move is valid.

        Args:
            col: The column to check if a piece can be dropped in.
        
        Returns:
            True if the move is valid, False otherwise.
        '''

        # Check if the column is full
        return self.board[0][col] == self.empty
    
    def check_winner(self):
        '''
        Checks if there is a winner.
        
        Returns:
            The token of the winner if there is one, None otherwise.
        '''

        for row in range(self.rows):
            for col in range(self.columns):
                token = self.board[row][col]
                if token != self.empty:
                    # Check for a horizontal win.
                    if col <= self.columns - 4:
                        if self.board[row][col+1] == token and self.board[row][col+2] == token and self.board[row][col+3] == token:
                            return token

                    # Check for a vertical win.
                    if row <= self.rows - 4:
                        if self.board[row+1][col] == token and self.board[row+2][col] == token and self.board[row+3][col] == token:
                            return token

                    # Check for a downward diagonal win.
                    if row <= self.rows - 4 and col <= self.columns - 4:
                        if self.board[row+1][col+1] == token and self.board[row+2][col+2] == token and self.board[row+3][col+3] == token:
                            return token

                    # Check for an upward diagonal win.
                    if row <= self.rows - 4 and col >= 3:
                        if self.board[row+1][col-1] == token and self.board[row+2][col-2] == token and self.board[row+3][col-3] == token:
                            return token

    def is_full(self):
        '''
        Checks if the board is full.
        
        Returns:
            True if the board is full, False otherwise.
        '''

        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] != self.empty:
                    return False
        return True

    def print_board(self):
        '''
        Prints the board.
        '''

        for row in self.board:
            for cell in row:
                if cell == self.empty:
                    print(cell, end='  ')
                else:
                    # print color player token
                    print(f'{cell}{self.token}', end='  ')
            print()
        print('  '.join(str(i+1) for i in range(self.columns)))

    def clear_board(self):
        '''
        Clears the board.
        '''

        self.board = [[self.empty for _ in range(self.columns)] for _ in range(self.rows)]

