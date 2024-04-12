import curses
import numpy as np
import sys

def main(stdscr, player_names, num_players, grid_size, symbols):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(False)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlight the active cell

    # Initialize the game board
    board = np.full((grid_size, grid_size), " ")
    current_player = 0
    pos = [0, 0]  # Initial position

    def draw_board():
        stdscr.clear()
        for y in range(grid_size):
            for x in range(grid_size):
                symbol = board[y][x]
                if [y, x] == pos:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y * 2, x * 4, f"|__{symbol}__|")
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y * 2, x * 4, f"|__{symbol}__|")
        stdscr.refresh()

    def check_win():
        # Check rows, columns, and diagonals for a win
        lines = []
        # Rows and columns
        lines.extend(board)
        lines.extend(board.T)
        # Diagonals
        diagonals = [board.diagonal(i) for i in range(-grid_size+1, grid_size)]
        diagonals.extend(np.fliplr(board).diagonal(i) for i in range(-grid_size+1, grid_size))
        lines.extend(diagonals)
        # Check if any line has a consecutive sequence of the same symbol of required length
        for line in lines:
            for symbol in symbols:
                if np.array_str(line).find(symbol * 5) != -1:
                    return True
        return False

    while True:
        draw_board()
        key = stdscr.getch()
        if key == curses.KEY_UP and pos[0] > 0:
            pos[0] -= 1
        elif key == curses.KEY_DOWN and pos[0] < grid_size - 1:
            pos[0] += 1
        elif key == curses.KEY_LEFT and pos[1] > 0:
            pos[1] -= 1
        elif key == curses.KEY_RIGHT and pos[1] < grid_size - 1:
            pos[1] += 1
        elif key == 10:  # Enter key to make a move
            y, x = pos
            if board[y][x] == " ":
                board[y][x] = symbols[current_player]
                if check_win():
                    stdscr.addstr(grid_size * 2, 0, f"{player_names[current_player]} wins!")
                    stdscr.refresh()
                    stdscr.getch()
                    return
                elif np.all(board != " "):
                    stdscr.addstr(grid_size * 2, 0, "It's a draw!")
                    stdscr.refresh()
                    stdscr.getch()
                    return
                current_player = (current_player + 1) % num_players

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tic_tac_toe.py <num_players> <grid_size>")
        sys.exit(1)
    num_players = int(sys.argv[1])
    grid_size = int(sys.argv[2])
    if not (5 <= grid_size <= 25):
        raise ValueError("Grid size must be between 5 and 25")
    player_names = []
    symbols = []
    for i in range(num_players):
        name = input(f"Enter player {i+1} name: ")
        symbol = input(f"Select a unique symbol for {name} (one character): ")
        while len(symbol) != 1 or symbol in symbols:
            symbol = input("Symbol must be one character and unique. Choose another symbol: ")
        player_names.append(name)
        symbols.append(symbol)
    curses.wrapper(main, player_names, num_players, grid_size, symbols)
