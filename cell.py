from graphics import Line, Point, Window


class Cell:
    def __init__(
        self,
        win: Window | None,
    ) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1: int = -1
        self._y1: int = -1
        self._x2: int = -1
        self._y2: int = -1
        self._win: Window | None = win

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        left: Line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right: Line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top: Line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom: Line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

        if self.has_left_wall:
            self._win.draw_line(left)
        else:
            self._win.draw_line(left, "white")

        if self.has_right_wall:
            self._win.draw_line(right)
        else:
            self._win.draw_line(right, "white")

        if self.has_top_wall:
            self._win.draw_line(top)
        else:
            self._win.draw_line(top, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom)
        else:
            self._win.draw_line(bottom, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if self._win is None:
            return

        fill_color: str = "red"
        if undo:
            fill_color = "gray"

        self_center: Point = self.get_center()
        to_cell_center: Point = to_cell.get_center()

        self._win.draw_line(Line(self_center, to_cell_center), fill_color)

    def get_center(self) -> Point:
        dx: int = abs(self._x1 - self._x2)
        dy: int = abs(self._y1 - self._y2)

        return Point(self._x1 + (dx // 2), self._y1 + (dy // 2))
