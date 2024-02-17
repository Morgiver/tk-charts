import sys
from tkinter import *

sys.path.append('./src')

from tk_charts import TkCharts

width = 500
height = 500
format = '%Y-%m-%d %H:%M:%S'

master = Tk()
master.geometry(f"{width}x{height}")

chart = TkCharts(master, width, height)
chart.pack(fill = BOTH, expand = YES)
chart.draw()

master.mainloop()