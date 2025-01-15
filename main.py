from graphics import Window
from maze import Maze


def main():
    num_rows: int = 12
    num_cols: int = 16
    margin: int = 50
    screen_x: int = 800
    screen_y: int = 600
    cell_size_x: int = (screen_x - 2 * margin) // num_cols
    cell_size_y: int = (screen_y - 2 * margin) // num_rows

    win = Window(screen_x, screen_y)
    _ = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    win.wait_for_close()


if __name__ == "__main__":
    main()
