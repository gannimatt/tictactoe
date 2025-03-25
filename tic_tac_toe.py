import curses
import numpy as np
import sys

def main(stdscr, player_names, num_players, grid_size, symbols):
    curses.curs_set(0)  # Set to 1 if you want a blinking cursor
    stdscr.nodelay(False)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Highlight current cell
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Regular cells

    board = np.full((grid_size, grid_size), " ")
    current_player = 0
    pos = [0, 0]

    def draw_board():
        stdscr.clear()
        for y in range(grid_size):
            for x in range(grid_size):
                symbol = board[y][x]
                cell = f"[{symbol}]"
                if [y, x] == pos:
                    stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                    stdscr.addstr(y, x * 4, cell)
                    stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x * 4, cell)
                    stdscr.attroff(curses.color_pair(2))

        stdscr.addstr(grid_size + 1, 0, f"{player_names[current_player]}'s turn ({symbols[current_player]})  ")
        stdscr.refresh()

    def check_win():
        for i in range(grid_size):
            if np.all(board[i, :] == board[i, 0]) and board[i, 0] != " ":
                return True
            if np.all(board[:, i] == board[0, i]) and board[0, i] != " ":
                return True
        if np.all(np.diagonal(board) == board[0, 0]) and board[0, 0] != " ":
            return True
        if np.all(np.diagonal(np.fliplr(board)) == board[0, -1]) and board[0, -1] != " ":
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
        elif key == 10:  # Enter key
            y, x = pos
            if board[y][x] == " ":
                board[y][x] = symbols[current_player]
                if check_win():
                    draw_board()
                    stdscr.addstr(grid_size + 2, 0, f"{player_names[current_player]} wins! Press any key.")
                    stdscr.getch()
                    return
                elif np.all(board != " "):
                    draw_board()
                    stdscr.addstr(grid_size + 2, 0, "It's a draw! Press any key.")
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
        name = input(f"Enter name for Player {i+1}: ")
        symbol = input(f"Choose a unique symbol for {name} (one character): ")
        while len(symbol) != 1 or symbol in symbols:
            symbol = input("Symbol must be one character and unique. Choose another: ")
        player_names.append(name)
        symbols.append(symbol)

    curses.wrapper(main, player_names, num_players, grid_size, symbols)
