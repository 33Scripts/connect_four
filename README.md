# Connect Four

A simple terminal-based Connect Four game built with Python. Enjoy a classic game of strategy with a straightforward and fun command-line interface.

## Features

- **Animated Gameplay:** Watch pieces drop into place.
- **Customizable Board:** Adjust the number of rows and columns via the settings.
- **Colorful Interface:** Uses [Colorama](https://pypi.org/project/colorama/) for colored player tokens.
- **Replayable:** Option to play again after each game.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/33Scripts/connect_four.git
   cd connect-four
   ```

2. **Set Up Environment:**
   Ensure you have Python 3.8 or later installed.

3. **Install Dependencies:**
   If using Poetry:
   ```bash
   poetry install --no-root
   ```
   Alternatively, install Colorama directly:
   ```bash
   pip install colorama
   ```

## How to Play

Run the game by executing:
```bash
python src/main.py
```
Follow the on-screen instructions to choose players, select colors, and start the game.

## Settings

Adjust the board dimensions in the **Settings** menu (accessible from the main menu) to create a custom playing field.

## License

This project is licensed under the [MIT License](LICENSE).
