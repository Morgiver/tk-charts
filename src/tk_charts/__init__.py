from tkinter import *

def draw_line(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_line(
        x1,
        canvas.winfo_reqheight() - y1,
        x2,
        canvas.winfo_reqheight() - y2,
        **kwargs
    )

def draw_rectangle(canvas: Canvas, x1: float, y1: float, x2: float, y2: float, **kwargs):
    canvas.create_rectangle(
        x1,
        canvas.winfo_reqheight() - y1,
        x2,
        canvas.winfo_reqheight() - y2,
        **kwargs
    )

def draw_text(canvas: Canvas, x: float, y: float, **kwargs):
    canvas.create_text(
        x,
        canvas.winfo_reqheight() - y,
        **kwargs
    )