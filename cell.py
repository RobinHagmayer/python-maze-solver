from graphics import Line, Point, Window


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

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        fill_color: str = "red"
        if undo:
            fill_color = "gray"

        self_center: Point = self.get_center()
        to_cell_center: Point = to_cell.get_center()

        self.__win.draw_line(Line(self_center, to_cell_center), fill_color)

    def get_center(self) -> Point:
        dx: int = abs(self.__x1 - self.__x2)
        dy: int = abs(self.__y1 - self.__y2)

        return Point(self.__x1 + (dx // 2), self.__y1 + (dy // 2))
