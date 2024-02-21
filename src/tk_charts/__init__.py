from tkinter import *

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
    def __init__(self, parent, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)
        self.parent = parent

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
        total_width     = self.width - self.height
        x_chevron_units = total_width / 10
        x_units         = (max(self.parent.datas) - min(self.parent.datas)) / 10

        for i in range(10):
            if i > 0 and i < 10:
                """ Draw the step line """
                draw_line(
                    self.canvas,
                    self.position.x + i * x_chevron_units,
                    self.position.y + self.height,
                    self.position.x + i * x_chevron_units,
                    self.position.y + self.height - self.height / 6,
                    fill = 'white'
                )

                """ Draw the value text """
                draw_text(
                    self.canvas,
                    self.position.x + i * x_chevron_units,
                    self.position.y + self.height - self.height / 3,
                    fill = 'white',
                    text = ''
                )

class YScaleView(ScaleView):
    """ Y scale view """
    def __init__(self, parent, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)
        self.parent = parent

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
        y_chevron_units = total_height / 10
        y_units = (max(self.parent.datas) - min(self.parent.datas)) / 10

        for i in range(10):
            if i > 0 and i < 9:
                """ Draw the step line """
                draw_line(
                    self.canvas,
                    self.position.x,
                    self.position.y + self.width + i * y_chevron_units,
                    self.position.x + self.width / 6,
                    self.position.y + self.width + i * y_chevron_units,
                    fill = 'white'
                )

                """ Draw the value text """
                draw_text(
                    self.canvas,
                    self.position.x + self.width / 2,
                    self.position.y + self.width + i * y_chevron_units,
                    fill = 'white',
                    text = y_units * i
                )

class DataView(Panel):
    """ Data View """
    def __init__(self, parent, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas, width, height)
        self.parent = parent
        self.style  = 'line'

    def draw_line_style(self):
        datas = self.parent.datas
        x_units = self.width / len(datas)
        y_units = self.height / max(datas) - min(datas)

        for i in range(len(datas)):
            if i > 0 and i < len(datas):
                x1 = self.position.x + i * x_units
                y1 = self.position.y + self.parent.x_scale_view.height + datas[i-1] * y_units
                x2 = self.position.x + (i + 1) * x_units
                y2 = self.position.y + self.parent.x_scale_view.height + datas[i] * y_units

                draw_line(self.canvas, x1, y1, x2, y2, fill = 'blue', width = 2)

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

        if self.style == 'line':
            self.draw_line_style()


class DataViewport(Entity):
    """ Data Viewport manage and draw all Panels (X and Y scalers and DataView) """
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(canvas)

        """ Setting scale data's """
        self.width          = width
        self.height         = height
        self.x_scale_height = 50
        self.y_scale_width  = 50
        self.datas          = None

        """ Dividing the Viewport in panels """
        self.x_scale_view = XScaleView(self, canvas, self.width, self.x_scale_height)
        self.y_scale_view = YScaleView(self, canvas, self.y_scale_width, self.height)
        self.data_view    = DataView(self, canvas, self.width - self.y_scale_width, self.height - self.x_scale_height)

        """ Updating panels positions """
        self.update_position(self.position.x, self.position.y)

    def update_datas(self, datas):
        self.datas = datas

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

class DrawFrame(Canvas):
    def __init__(self, master, width: int, height: int, **kwargs):
        super().__init__(master, width = width, height = height, **kwargs)

        self.chart  = master
        self.bind('<Button-1>', self.on_button_down)
        self.bind('<ButtonRelease-1>', self.on_button_release)

    def draw_arc(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        self.create_arc(x1, self.winfo_reqheight() - y1, x2, self.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

    def draw_bitmap(self, x: float, y: float, **kwargs):
        self.create_bitmap(x, self.winfo_reqheight() - y, tags = 'Entity', **kwargs)

    def draw_image(self, x: float, y: float, **kwargs):
        self.create_image(x, self.winfo_reqheight() - y, tags = 'Entity', **kwargs)

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        self.create_line(x1, self.winfo_reqheight() - y1, x2, self.winfo_reqheight() - y2, tags = 'Entity',  **kwargs)

    def draw_oval(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        self.create_oval(x1, self.winfo_reqheight() - y1, x2, self.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

    def draw_polygon(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        self.create_polygon(x1, self.winfo_reqheight() - y1, x2, self.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

    def draw_rectangle(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        self.create_rectangle(x1, self.winfo_reqheight() - y1, x2, self.winfo_reqheight() - y2, tags = 'Entity', **kwargs)

    def draw_text(self, x: float, y: float, **kwargs):
        self.create_text(x, self.winfo_reqheight() - y, tags = 'Entity', **kwargs)

    def draw(self):
        pass

    def on_button_down(self, event):
        pass

    def on_button_release(self, event):
        pass

    def rescale(self):
        pass

class XScaleFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width, height, **kwargs)

class YScaleFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width, height, **kwargs)

class DataChartFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width = width, height = height, **kwargs)

class TkCharts(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.data_chart_frame = DataChartFrame(self, 450, 450, bg = 'grey')
        self.data_chart_frame.grid(column = 0, row = 0, sticky=N+S+E+W)

        self.y_scale_frame = YScaleFrame(self, 50, 450, bg = 'black')
        self.y_scale_frame.grid(column = 1, row = 0, sticky=N+S+E+W)

        self.x_scale_frame = XScaleFrame(self, 450, 50, bg = 'black')
        self.x_scale_frame.grid(column = 0, row = 1, sticky=N+S+E+W)

        self.bind('<Configure>', self.on_resize)

    def on_resize(self, event):
        self.data_chart_frame.configure(width = event.width - self.x_scale_frame.winfo_height(), height = event.height - self.y_scale_frame.winfo_width())
        self.draw()

    def draw(self):
        self.data_chart_frame.draw()
        self.y_scale_frame.draw()
        self.x_scale_frame.draw()