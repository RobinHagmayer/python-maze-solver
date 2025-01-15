import time
from cell import Cell
from graphics import Window


class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window) -> None:
        self._cells: list[list[Cell]] = []
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window = win

        self._create_cells()

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
        cell: Cell = self._cells[col][row]
        x1: int = self._x1 + col * self._cell_size_x
        y1: int = self._y1 + row * self._cell_size_y
        cell.draw(x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y)
        self._animate()

    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)
