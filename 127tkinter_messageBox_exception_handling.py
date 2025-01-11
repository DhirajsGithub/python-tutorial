from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from tkinter import font

win = tk.Tk()
win.title('message box')

# label frame 
label_frame = tk.LabelFrame(win, text="Contact Details" )
label_frame.grid(row=0, column=0, padx=40, pady=10)

#labels
name_label = ttk.Label(label_frame, text="Enter you name bsdk", font=('helvetica', 14))
age_label = ttk.Label(label_frame, text="Enter you age bsdk", font=('helvetica', 14))

#entry box variables
name_var = tk.StringVar()
age_var = tk.IntVar()

# entry box
name_entry = ttk.Entry(label_frame, width=36, textvariable=name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable=age_var)

# grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)


def pop_up ():
    # m_box.showinfo('title', 'content of this box!!')
    # m_box.showerror('title', 'erroe') 
    # m_box.showwarning()
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error', 'Please fill name and age')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('titile', 'only digits allowed in age field')
        else :
            if age < 18 :
                m_box.showwarning('titile', 'underage')
            m_box.showinfo('title', f"hello {name} to the sexual conent, so you admit you are {age} yrs old ha")
            print(f"hello {name} to the sexual conent, so you admit you are {age} yrs old ha")

# button
submit_btn = ttk.Button(win, text="Submit", command=pop_up)
submit_btn.grid(row=1, columnspan=2, padx=40)




win.mainloop()
