# terminal-tic-tac-toe

## Overview

A terminal-based multiplayer Tic Tac Toe game built in Python using the `curses` library. The game allows dynamic grid sizes (between 5x5 and 25x25) and supports any number of players (each with a unique symbol).

This is a fun console-based challenge to see who can dominate the grid — best played right in the terminal!

## Features

- Supports 2 or more players
- Customizable grid size (5x5 to 25x25)
- Live keyboard navigation using arrow keys
- Color-highlighted current cell and turn indicator
- Win and draw detection
- Cross-platform support (Windows and Unix-like systems)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gannimatt/terminal-tic-tac-toe.git
   cd terminal-tic-tac-toe
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   > On Windows, `windows-curses` is installed to enable `curses` support.

## Usage

Run the game from your **system terminal (not an IDE)**:

```bash
python tic_tac_toe.py <num_players> <grid_size>
```

- `num_players`: Number of players (e.g., 2, 3, 4, ...)
- `grid_size`: Size of the grid (must be between 5 and 25)

### Example

```bash
python tic_tac_toe.py 3 7
```

> This launches a 7x7 board for 3 players. Each player will be prompted to enter their name and a unique one-character symbol.

## Controls

- Use **arrow keys** to move your cursor around the board.
- Press **Enter** to place your symbol in an empty cell.
- The game ends when a player wins or the board fills in a draw.

## Notes

- Make sure to run the script in a **real terminal window**. IDEs like VS Code or PyCharm might not render `curses` correctly.
- Symbols must be **single characters** and **unique for each player**.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests and forks are welcome! If you’d like to improve the game or add features (AI bot, scoreboard, animations), feel free to contribute.
