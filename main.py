from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)

    cell1: Cell = Cell(win)
    cell1.has_left_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(125, 125, 200, 200)
    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.draw(225, 225, 250, 250)
    cell2.draw_move(cell3, undo=True)

    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(300, 300, 500, 500)

    win.wait_for_close()


if __name__ == "__main__":
    main()
