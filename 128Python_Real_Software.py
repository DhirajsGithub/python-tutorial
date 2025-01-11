import tkinter as tk 
from tkinter import ttk
import _tkinter 
from tkinter import font, colorchooser, filedialog, messagebox
import os 

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad text editor')
main_application.wm_iconbitmap('icon.ico')


################################# main Menu #########################################
#$$$$$$$$$$$$$$$$$$$$$$$$$$  end main menu $$$$$$$$$$$$$$$$$$$$$$$$$$#######

main_menu = tk.Menu()
file = tk.Menu(main_menu)
edit = tk.Menu(main_menu)
view = tk.Menu(main_menu)
color_theme = tk.Menu(main_menu)

# cascade without it you can't see the menu
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)


################################# toolbar #########################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$  end toolbar $$$$$$$$$$$$$$$$$$$$$$$$$$#######


################################# text editor #########################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$  end text editor $$$$$$$$$$$$$$$$$$$$$$$$$$#######


################################# main status bar #########################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$  end main status bar $$$$$$$$$$$$$$$$$$$$$$$$$$#######


################################# main Menu function #########################################


#$$$$$$$$$$$$$$$$$$$$$$$$$$  end main menu function $$$$$$$$$$$$$$$$$$$$$$$$$$#######


main_application.mainloop()
