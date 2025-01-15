from tkinter import BOTH, Canvas, Tk
from typing import override


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    @override
    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


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
        self._root: Tk = Tk()
        self._root.title("Python Maze Solver")
        self._canvas: Canvas = Canvas(
            self._root, bg="white", height=height, width=width
        )
        self._canvas.pack(fill=BOTH, expand=1)
        self._running: bool = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self._running = False

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self._canvas, fill_color)
