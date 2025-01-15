import random
import time

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None
    ) -> None:
        self._cells: list[list[Cell]] = []
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window | None = win
        if seed is not None:
                random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        for _ in range(self._num_cols):
            col_cells: list[Cell] = []
            for _ in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col: int, row: int) -> None:
        if self._win is None:
            return
        cell: Cell = self._cells[col][row]
        x1: int = self._x1 + col * self._cell_size_x
        y1: int = self._y1 + row * self._cell_size_y
        cell.draw(x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        entrance_cell: Cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell_row: int = self._num_rows - 1
        exit_cell_col: int = self._num_cols - 1
        exit_cell: Cell = self._cells[exit_cell_col][exit_cell_row]
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_cell_col, exit_cell_row)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True

        while True:
            next_index_list: list[tuple[int, int]] = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index: int = random.randrange(len(next_index_list))
            next_index: tuple[int, int] = next_index_list[direction_index]

            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for row in col:
                row.visited = False
