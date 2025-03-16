from board import Board
from utils import clear_screen

class Game:
    def __init__(self, player1, player2, rows, columns):
        rows = min(max(rows, 4), 10)
        self.columns = min(max(columns, 4), 10)
        self.board = Board(rows, self.columns)
        self.players = [player1, player2]
        self.current_player = player1
    
    def switch_player(self):
        '''
        Switches the current player.
        '''
        
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play(self):
        while True:
            clear_screen()
            self.board.print_board()
            try:
                col = int(input(f'{self.current_player.name}, enter a column (1-{self.columns}): ')) - 1
            except ValueError:
                input(f'Please enter an integer between 1 and {self.columns}. Press Enter to continue.')
                continue
                
            if 0 <= col < self.columns:
                if self.board.drop_piece(col, self.current_player.color):
                    if self.board.check_winner():
                        clear_screen()
                        self.board.print_board()
                        print(f'{self.current_player.name} wins!')
                        break
                    if self.board.is_full():
                        print("The board is full. It's a tie!")
                        break

                    self.switch_player()
                else:
                    input('Column is full. Try another column. Press Enter to continue.')
            else:
                input(f'Column out of range. Choose a column between 1 and {self.columns}. Press Enter to continue.')
                continue
        
        if input('Would you like to play again? Y/n: ').upper() == 'Y':
            self.board.clear_board()
            self.play()
