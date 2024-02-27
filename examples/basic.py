import sys
import numpy as np
from tkinter import *

sys.path.append('./src')

from tk_charts import TkCharts

datas = np.random.uniform(-50.0, 50.0, size=(250,))
print(datas)
width  = 500
height = 500

master = Tk()
master.geometry(f"{width}x{height}")

chart = TkCharts(master)
chart.pack(fill = BOTH, expand = YES)
chart.update_datas(datas)
chart.draw()

master.mainloop()