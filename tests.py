import unittest

from cell import Cell
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self) -> None:
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entry_and_exit_wall_removal(self) -> None:
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell: Cell = m1._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)
        exit_cell: Cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_maze_reset_visited(self) -> None:
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        for col in m1._cells:
            for row in col:
                self.assertFalse(row.visited)


if __name__ == "__main__":
    _ = unittest.main()
