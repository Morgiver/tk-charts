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

class ScaleView(Panel):
    """ ScaleView is a base class to define standard method and data for axes scaling controls"""
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)

        """ Scale is the unit per pixels """
        self.scale = 1.0

        """ Minimum value visible """
        self.min_value = 0.0

        """ Maximum value visible """
        self.max_value = 0.0
    
    def update_scale(self, new_value: float):
        self.scale = new_value

class XScaleView(ScaleView):
    """ X axis scale view """
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)

    def draw(self):
        """ Draw the top horizontal line """
        draw_line(
            self.canvas,
            self.position.x, 
            self.position.y + self.height, 
            self.position.x + self.width - self.height / 2,
            self.position.y + self.height,
            fill = 'white',
            width = 2
        )

        """ Defining space width between every steps """
        total_width = self.width - self.height
        units = total_width / 10

        for i in range(10):
            if i > 0 and i < 10:
                """ Draw the step line """
                draw_line(
                    self.canvas,
                    self.position.x + i * units,
                    self.position.y + self.height,
                    self.position.x + i * units,
                    self.position.y + self.height - self.height / 6,
                    fill = 'white'
                )

                """ Draw the value text """
                draw_text(
                    self.canvas,
                    self.position.x + i * units,
                    self.position.y + self.height - self.height / 3,
                    fill = 'white',
                    text = i * units * self.scale
                )

class YScaleView(ScaleView):
    """ Y scale view """
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)

    def draw(self):
        """ Draw the left vertical line """
        draw_line(
            self.canvas,
            self.position.x, 
            self.position.y + self.width / 2, 
            self.position.x,
            self.position.y + self.height,
            fill = 'white',
            width = 2
        )

        total_height = self.height
        units = total_height / 10

        for i in range(10):
            if i > 0 and i < 9:
                """ Draw the step line """
                draw_line(
                    self.canvas,
                    self.position.x,
                    self.position.y + self.width + i * units,
                    self.position.x + self.width / 6,
                    self.position.y + self.width + i * units,
                    fill = 'white'
                )

                """ Draw the value text """
                draw_text(
                    self.canvas,
                    self.position.x + self.width / 2,
                    self.position.y + self.width + i * units,
                    fill = 'white',
                    text = i * units * self.scale
                )