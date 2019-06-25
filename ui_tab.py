import tkinter as tk
from tkinter import ttk




win = tk.Tk()

win.title("Python GUI")


tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'File Handling')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Text Processing')


tabControl.pack(expand = 1, fill = "both")




win.mainloop()