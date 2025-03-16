from player import Player
from game import Game
from colorama import Fore
from utils import clear_screen, get_settings, set_settings
import colorama



def main_menu():
    while True:
        clear_screen()
        print(r'''   
   ____                            _     _  _   
  / ___|___  _ __  _ __   ___  ___| |_  | || |  
 | |   / _ \| '_ \| '_ \ / _ \/ __| __| | || |_ 
 | |__| (_) | | | | | | |  __/ (__| |_  |__   _|
  \____\___/|_| |_|_| |_|\___|\___|\__|    |_|  
                                                ''')
        print("1. Play")
        print("2. Settings")
        print("3. Rules")
        print("4. Quit")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            settings_menu()
        elif choice == "3":
            show_rules()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            input("Invalid option. Press Enter to continue...")

def play_game():
    clear_screen()
    colorama.init(autoreset=True)
    # Load settings (rows and columns) from settings.json
    settings = get_settings()
    rows = settings.get('rows')
    columns = settings.get('columns')

    print(f"Game Settings: {rows} rows x {columns} columns\n")
    
    # Player setup (existing code from main.py)
    player1_name = input('Player 1, please enter your name: ')
    player2_name = input('Player 2, please enter your name: ')
    clear_screen()
    
    color_map = {
        'Red': Fore.RED,
        'Blue': Fore.BLUE,
        'Green': Fore.GREEN,
        'Yellow': Fore.YELLOW,
        'Magenta': Fore.MAGENTA,
        'Cyan': Fore.CYAN,
    }
    
    for color in color_map:
        print(f'{color_map[color]}{color}')
    
    chosen_color = input(f'{player1_name}, choose your color: ').strip().capitalize()
    while chosen_color not in color_map:
        print('Invalid color. Please choose from the above colors.')
        chosen_color = input(f'{player1_name}, choose your color: ').strip().capitalize()
    player1_color = color_map[chosen_color]
    color_map.pop(chosen_color)
    clear_screen()
    
    for color in color_map:
        print(f'{color_map[color]}{color}')
    
    chosen_color = input(f'{player2_name}, choose your color: ').strip().capitalize()
    while chosen_color not in color_map:
        print('Invalid color. Please choose from the above colors.')
        chosen_color = input(f'{player2_name}, choose your color: ').strip().capitalize()
    player2_color = color_map[chosen_color]
    
    player1 = Player(player1_name, player1_color)
    player2 = Player(player2_name, player2_color)
    game = Game(player1, player2, rows, columns)
    game.play()
    
    # After the game, return to the main menu
    input("Press Enter to return to the main menu...")

def settings_menu():
    clear_screen()
    settings = get_settings()
    rows = settings.get('rows')
    columns = settings.get('columns')
    
    print(f'''Settings
--------------------------------------------------
1. Rows: {settings['rows']}
2. Columns: {settings['columns']}
--------------------------------------------------
''')
    change = input("Do you want to change the settings? (Y/n): ").strip().lower()
    if change == 'y':
        try:
            rows = int(input("Enter number of rows: "))
            while rows < 4 or rows > 10:
                print("Rows must be between 4 and 10.")
                rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
            while columns < 4 or columns > 10:
                print("Columns must be between 4 and 10.")
                columns = int(input("Enter number of columns: "))
            settings['rows'] = rows
            settings['columns'] = columns
            set_settings(settings)
            print("Settings updated!")
        except ValueError:
            print("Invalid input. Settings not changed.")
    input("Press Enter to return to the main menu...")

def show_rules():
    clear_screen()
    settings = get_settings()
    rows = settings.get('rows')
    columns = settings.get('columns')
    
    print(f'''Game Rules
--------------------------------------------------
1. The board has {rows} rows and {columns} columns.
2. Players take turns to drop their pieces in a column.
3. The first player to get four of their pieces in a row (horizontally, vertically, or diagonally) wins.
4. If the board is full and there is no winner, the game is a tie.
--------------------------------------------------
''')
    input("Press Enter to return to the main menu...")


if __name__ == '__main__':
    main_menu()
