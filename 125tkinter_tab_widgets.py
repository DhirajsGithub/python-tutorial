from cProfile import label
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("TAB control")
nb = ttk.Notebook(win)     # creating nb instance
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text="ONE")
nb.add(page2, text="TWO")
# nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')      # pack is used coz on the next page lines of first page should not be visible

label = ttk.Label(page1, text="this is page one")
label.grid(row=0, column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0, column=1)

labe2 = ttk.Label(page2, text="this is page one")
labe2.grid(row=0, column=0)

win.mainloop()