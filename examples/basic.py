import sys
from tkinter import *

sys.path.append('./src')

from tk_charts import TkCharts

format = '%Y-%m-%d %H:%M:%S'

master = Tk()
master.geometry("1000x1000")

chart = TkCharts(master, 1000, 1000)
chart.pack(fill = BOTH, expand = YES)
chart.draw()

master.mainloop()