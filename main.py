from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        _ = canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root: Tk = Tk()
        self.__root.title("Python Maze Solver")
        self.__canvas: Canvas = Canvas(
            self.__root, bg="white", height=height, width=width
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running: bool = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)


class Cell:
    def __init__(
        self,
        win: Window,
    ) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1: int = -1
        self.__y1: int = -1
        self.__x2: int = -1
        self.__y2: int = -1
        self.__win: Window = win

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            left: Line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left)
        if self.has_right_wall:
            right: Line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right)
        if self.has_top_wall:
            top: Line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top)
        if self.has_bottom_wall:
            bottom: Line = Line(
                Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)
            )
            self.__win.draw_line(bottom)


def main():
    win = Window(800, 600)

    cell: Cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(225, 225, 250, 250)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(300, 300, 500, 500)

    win.wait_for_close()


if __name__ == "__main__":
    main()
