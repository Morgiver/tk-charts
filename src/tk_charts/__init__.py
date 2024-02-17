from tkinter import *

""" Drawing function : Inverting Y axis in every functions """
def draw_arc(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_arc(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, **kwargs)

def draw_bitmap(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_bitmap(x, canvas.winfo_reqheight() - y, **kwargs)

def draw_image(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_image(x, canvas.winfo_reqheight() - y, **kwargs)

def draw_line(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_line(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2,  **kwargs)

def draw_oval(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_oval(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, **kwargs)

def draw_polygon(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_polygon(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, **kwargs)

def draw_rectangle(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_rectangle(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, **kwargs)

def draw_text(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_text(x, canvas.winfo_reqheight() - y, **kwargs)

class Position:
    """ X and Y axis Position coordinate in the Canvas"""
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

class Entity:
    """ Every drawable thing is an Entity and has a Canvas class, Postion class and draw function """
    def __init__(self, canvas: Canvas) -> None:
        self.canvas   = canvas
        self.position = Position()

    def update_position(self, x: float, y: float):
        self.position.x = x
        self.position.y = y

    def draw(self):
        pass

class Panel(Entity):
    """ Panel is a rectangle in the Canvas defining a new Context and Origin """
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas)

        self.width  = width
        self.height = height