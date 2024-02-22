import sys
from tkinter import *

sys.path.append('./src')

from tk_charts import TkCharts

datas = [1.0, 2.5, 8.6, 6.21, 12.0, 15.0, 9.70, 8.30, 9.90, 15.0]

width  = 500
height = 500
format = '%Y-%m-%d %H:%M:%S'

master = Tk()
master.geometry(f"{width}x{height}")

chart = TkCharts(master)
chart.pack(fill = BOTH, expand = YES)
chart.update_datas(datas)
#chart.draw()

master.mainloop()