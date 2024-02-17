from tkinter import *

""" 
    Drawing function : 
        - Inverting Y axis in every functions
        - Add 'Entity' tag
"""
def draw_arc(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_arc(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

def draw_bitmap(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_bitmap(x, canvas.winfo_reqheight() - y, tags = 'Entity', **kwargs)

def draw_image(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_image(x, canvas.winfo_reqheight() - y, tags = 'Entity', **kwargs)

def draw_line(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_line(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, tags = 'Entity',  **kwargs)

def draw_oval(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_oval(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

def draw_polygon(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_polygon(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

def draw_rectangle(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_rectangle(x1, canvas.winfo_reqheight() - y1, x2, canvas.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

def draw_text(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_text(x, canvas.winfo_reqheight() - y, tags = 'Entity', **kwargs)

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

class DataView(Panel):
    """ Data View """
    def __init__(self, parent, width: int, height: int) -> None:
        super().__init__(parent.canvas, width, height)
        self.parent = parent
        self.style  = 'candles'
        self.datas  = []

    def update_datas(self):
        # TODO
        pass

    def update_x_scale(self):
        # TODO
        pass 

    def update_y_scale(self):
        # TODO
        pass

    def draw(self):
        """ Draw outline borders """
        draw_rectangle(
            self.parent.canvas,
            self.position.x,
            self.position.y + self.parent.y_scale_width,
            self.position.x + self.width,
            self.position.y + self.height + self.parent.y_scale_width,
            outline = 'grey'
        )

class DataViewport(Entity):
    """ Data Viewport manage and draw all Panels (X and Y scalers and DataView) """
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas)

        """ Setting scale data's """
        self.width          = width
        self.height         = height
        self.x_scale_height = 50
        self.y_scale_width  = 50

        """ Dividing the Viewport in panels """
        self.x_scale_view = XScaleView(canvas, self.width, self.x_scale_height)
        self.y_scale_view = YScaleView(canvas, self.y_scale_width, self.height)
        self.data_view    = DataView(self, self.width - self.y_scale_width, self.height - self.x_scale_height)

        """ Updating panels positions """
        self.update_position(self.position.x, self.position.y)
    
    def resize(self, width: int, height: int):
        self.width  = width
        self.height = height

        self.data_view.width  = self.width - self.y_scale_width
        self.data_view.height = self.height - self.x_scale_height

        self.x_scale_view.width  = self.width
        self.x_scale_view.height = self.x_scale_height

        self.y_scale_view.width  = self.y_scale_width
        self.y_scale_view.height = self.height

    def update_x_scale(self, new_value: float):
        self.x_scale_view.update_scale(new_value)

    def update_y_scale(self, new_value: float):
        self.y_scale_view.update_scale(new_value)

    def update_position(self, x: float, y: float):
        """ Update the X and Y coordinates """
        self.position.x = x
        self.position.y = y

        """ Updating panels positions """
        self.data_view.update_position(
            self.position.x,
            self.position.y
        )
        
        self.x_scale_view.update_position(
            self.position.x, 
            self.position.y
        )

        self.y_scale_view.update_position(
            self.position.x + self.data_view.width,
            self.position.y
        )
    
    def reset_viewport(self):
        """ Deleting all drawable object tagged as 'Entity' in the Canvas """
        self.canvas.delete('Entity')

        """ Reseting the background """
        draw_rectangle(
            self.canvas,
            self.position.x, 
            self.position.y,
            self.position.x + self.width,
            self.position.y + self.height,
            fill = 'black'
        )

    def draw(self):
        """ Reseting the viewport """
        self.reset_viewport()

        """ Drawing panels """
        self.data_view.draw()
        self.y_scale_view.draw()
        self.x_scale_view.draw()

        """ Borders Rectangle """
        draw_rectangle(
            self.canvas,
            self.position.x, 
            self.position.y,
            self.position.x + self.width,
            self.position.y + self.height,
            outline = 'grey'
        )

class TkCharts(Frame):
    def __init__(self, master, width: int, height: int):
        super().__init__(master)

        self.canvas = Canvas(self, width = width, height = height)
        self.canvas.pack(fill = BOTH, expand = YES)

        self.bind('<Configure>', self.on_resize)

        self.viewport = DataViewport(self.canvas, width, height)
    
    def on_resize(self, event):
        self.canvas.config(width = event.width, height = event.height)
        self.viewport.update_position(0.0, 0.0)
        self.viewport.resize(event.width, event.height)
        self.viewport.draw()
    
    def draw(self):
        self.viewport.draw()
