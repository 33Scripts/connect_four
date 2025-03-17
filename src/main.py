from player import Player
from game import Game
from colorama import init, Fore
from utils import clear_screen, get_settings, set_settings


def main_menu():
    """Display the main menu and handle user navigation.

    Presents four options to the user:
        1. Play - Start a new game
        2. Settings - Adjust game parameters
        3. Rules - View game instructions
        4. Quit - Exit the game
    """
    while True:
        clear_screen()
        # ASCII art logo
        ascii_art = r"""
   ____                            _     _  _   
  / ___|___  _ __  _ __   ___  ___| |_  | || |  
 | |   / _ \| '_ \| '_ \ / _ \/ __| __| | || |_ 
 | |__| (_) | | | | | | |  __/ (__| |_  |__   _|
  \____\___/|_| |_|_| |_|\___|\___|\__|    |_|  
                                                """
        # Remove leading newline from ASCII art
        print(ascii_art.lstrip("\n"))
        # Menu options
        print("1. Play")
        print("2. Settings")
        print("3. Rules")
        print("4. Quit")

        choice = input("Select an option (1-4): ").strip()

        # Handle user selection
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
    """Start a new Connect Four game.

    Sets up players with names and colors, then initializes and runs
    the game with current board settings from settings file.
    """
    init(autoreset=True)  # Initialize colorama
    clear_screen()

    # Load board dimensions from settings
    settings = get_settings()
    rows = settings.get("rows")
    columns = settings.get("columns")

    print(f"Game Settings: {rows} rows x {columns} columns\n")

    # Get player names
    while True:
        player1_name = input("Player 1, please enter your name: ").strip().capitalize()
        if player1_name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    while True:
        player2_name = input("Player 2, please enter your name: ").strip().capitalize()
        if player2_name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    # Available colors for player pieces
    color_map = {
        "Red": Fore.RED,
        "Blue": Fore.BLUE,
        "Green": Fore.GREEN,
        "Yellow": Fore.YELLOW,
        "Magenta": Fore.MAGENTA,
        "Cyan": Fore.CYAN,
    }

    # Select colors for each player
    player1_color = choose_color(player1_name, color_map)
    # Remove player1's color from available options
    color_map.pop(player1_color[1])
    player2_color = choose_color(player2_name, color_map)

    # Create player objects and start the game
    player1 = Player(player1_name, player1_color[0])
    player2 = Player(player2_name, player2_color[0])
    game = Game(player1, player2, rows, columns)
    game.play()

    # Return to the main menu after game ends
    input("Press Enter to return to the main menu...")


def settings_menu():
    """Display and modify game settings.

    Allows the user to view and change the number of rows and columns
    for the game board. Changes are saved to the settings file.
    """
    clear_screen()
    # Load current settings
    settings = get_settings()
    rows = settings.get("rows")
    columns = settings.get("columns")

    # Display current settings
    print(f"""Settings
--------------------------------------------------
1. Rows: {settings["rows"]}
2. Columns: {settings["columns"]}
--------------------------------------------------
""")

    # Ask if user wants to modify settings
    change = input("Do you want to change the settings? (Y/n): ").strip().lower()

    if change == "y":
        try:
            # Get and validate new row count
            rows = int(input("Enter number of rows: "))
            while rows < 4 or rows > 10:
                print("Rows must be between 4 and 10.")
                rows = int(input("Enter number of rows: "))

            # Get and validate new column count
            columns = int(input("Enter number of columns: "))
            while columns < 4 or columns > 10:
                print("Columns must be between 4 and 10.")
                columns = int(input("Enter number of columns: "))

            # Save new settings
            settings["rows"] = rows
            settings["columns"] = columns
            set_settings(settings)
            print("Settings updated!")
        except ValueError:
            print("Invalid input. Settings not changed.")

    input("Press Enter to return to the main menu...")


def show_rules():
    """Display the game rules to the player.

    Shows a description of how to play Connect Four with the current
    board dimensions from settings.
    """
    clear_screen()
    # Load current settings for rule display
    settings = get_settings()
    rows = settings.get("rows")
    columns = settings.get("columns")

    # Display rules
    print(f"""Game Rules
--------------------------------------------------
1. The board has {rows} rows and {columns} columns.
2. Players take turns to drop their pieces in a column.
3. The first player to get four of their pieces in a row (horizontally, vertically, or diagonally) wins.
4. If the board is full and there is no winner, the game is a tie.
--------------------------------------------------
""")
    input("Press Enter to return to the main menu...")


def choose_color(player_name, color_map):
    """Allow a player to select their piece color.

    Args:
        player_name (str): The name of the player choosing a color
        color_map (dict): Dictionary mapping color names to colorama color codes

    Returns:
        tuple: A tuple containing (colorama_color_code, color_name)
    """
    clear_screen()
    # Create a list of available colors
    color_list = list(color_map.keys())

    # Display color options with their visual representation
    for idx, color in enumerate(color_list, start=1):
        print(f"{idx}. {color_map[color]}{color}")

    # Get and validate player color choice
    while True:
        try:
            choice = int(input(f"{player_name}, choose your color (1-{len(color_list)}): "))
            if 1 <= choice <= len(color_list):
                selected_color = color_list[choice - 1]
                return color_map[selected_color], selected_color
            else:
                print("Invalid color selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nThanks for playing!")
