from tkinter import *

NEUTRAL         = 'NEUTRAL'
BUTTON_RELEASED = 'BUTTON_RELEASED'
BUTTON_DOWN     = 'BUTTON_DOWN'


class DrawFrame(Canvas):
    def __init__(self, master, width: int, height: int, **kwargs):
        super().__init__(master, width = width, height = height, **kwargs)

        self.chart = master

        self.bind('<Button-1>', self.on_left_button_down)
        self.bind('<ButtonRelease-1>', self.on_left_button_release)

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

    def on_left_button_down(self, event):
        pass

    def on_left_button_release(self, event):
        pass

    def rescale(self):
        pass

    def reset(self):
        """ Deleting all drawable object tagged as 'Entity' in the Canvas """
        self.delete('Entity')

class XScaleFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width, height, **kwargs)
    
    def draw(self):
        self.reset()
        self.draw_line(
            0.0, 
            self.winfo_height(),
            self.winfo_width(),
            self.winfo_height(),
            fill = 'white',
            width = 2
        )

        """ Defining space width between every steps """
        total_width     = self.winfo_width()
        x_chevron_units = total_width / 10
        x_units         = (max(self.chart.datas) - min(self.chart.datas)) / 10

        for i in range(10):
            if i > 0 and i < 10:
                """ Draw the step line """
                self.draw_line(
                    i * x_chevron_units,
                    self.winfo_height(),
                    i * x_chevron_units,
                    self.winfo_height() - 10,
                    fill = 'white'
                )

                """ Draw the value text """
                self.draw_text(
                    i * x_chevron_units,
                    self.winfo_height() - 25,
                    fill = 'white',
                    text = "{:.2f}".format(x_units * i)
                )

class YScaleFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width, height, **kwargs)

    def draw(self):
        self.reset()
        self.draw_line(
            0.0, 
            0.0,
            0.0,
            self.winfo_reqheight(),
            fill = 'white',
            width = 2
        )

        total_height = self.winfo_height()
        y_chevron_units = total_height / 10
        y_units = (max(self.chart.datas) - min(self.chart.datas)) / 10

        for i in range(10):
            if i > 0 and i < 10:
                """ Draw the step line """
                self.draw_line(
                    0.0,
                    i * y_chevron_units,
                    10,
                    i * y_chevron_units,
                    fill = 'white'
                )

                """ Draw the value text """
                self.draw_text(
                    25,
                    i * y_chevron_units,
                    fill = 'white',
                    text = "{:.2f}".format(y_units * i)
                )

class DataChartFrame(DrawFrame):
    def __init__(self, master, width: int, height: int, **kwargs) -> None:
        super().__init__(master, width = width, height = height, **kwargs)
    
    def draw(self):
        self.reset()

        datas = self.chart.datas
        x_units = self.winfo_width() / len(datas)
        y_units = self.winfo_height() / max(datas) - min(datas)

        for i in range(len(datas)):
            if i > 0 and i < len(datas):
                x1 = i * x_units
                y1 = datas[i-1] * y_units
                x2 = (i + 1) * x_units
                y2 = datas[i] * y_units

                self.draw_line(x1, y1, x2, y2, fill = 'blue', width = 1)

class TkCharts(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.datas      = None
        self.base_data  = 500
        self.base_scale = 65

        self.data_chart_frame = DataChartFrame(self, self.base_data, self.base_data, highlightthickness = 0, bg = 'black')
        self.data_chart_frame.grid(column = 0, row = 0, sticky=N+S+E+W)

        self.y_scale_frame = YScaleFrame(self, self.base_scale, self.base_data, highlightthickness = 0, bg = 'black')
        self.y_scale_frame.grid(column = 1, row = 0, sticky=N+S+E+W)

        self.x_scale_frame = XScaleFrame(self, self.base_data, self.base_scale, highlightthickness = 0, bg = 'black')
        self.x_scale_frame.grid(column = 0, row = 1, sticky=N+S+E+W)

        self.ctrl_frame = Frame(self, highlightthickness = 0, bg = 'black')
        self.ctrl_frame.grid(column = 1, row = 1, sticky=N+S+E+W)

        # Controls states
        self.left_button = NEUTRAL

        self.bind('<Configure>', self.on_resize)

    def update_datas(self, new_datas):
        self.datas = new_datas

    def on_resize(self, event):
        self.data_chart_frame.configure(width = event.width - self.base_scale, height = event.height - self.base_scale)
        self.y_scale_frame.configure(width = self.base_scale, height = event.height - self.base_scale)
        self.x_scale_frame.configure(width = event.width - self.base_scale, height = self.base_scale)
        self.draw()

    def draw(self):
        self.data_chart_frame.draw()
        self.y_scale_frame.draw()
        self.x_scale_frame.draw()