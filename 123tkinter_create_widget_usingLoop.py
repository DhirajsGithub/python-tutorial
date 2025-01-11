# for loop 
import tkinter as tk
from tkinter import Grid, ttk

win = tk.Tk()
win.title("LOOP")

# name_label = ttk.Label(win, text="enter your name: ")
# name_label.grid(row=0, column=0, sticky=tk.W)

labels = ["your name", "your age", "your email", "your country", "your state", "your city"]
for i in range(len(labels)):
    cur_label = "label" + str(i)
    cur_label = ttk.Label(win, text=("What is your "+ labels[i].split(" ")[1] +" : "))
    cur_label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)


# entry box 
# name_var = tk.StringVar()
# name_entry = ttk.Entry(win, width=16, textvariable=name_var)
# name_entry.grid(row=0, column=1)

user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'email' : tk.StringVar(),
    'country' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar()
}

counter = 0
for i in user_info:
    curl_entry = "entry" +i
    curl_entry = ttk.Entry(win, width=16, textvariable=user_info[i])
    curl_entry.grid(row=counter, column=1, padx=10, pady=5)
    counter +=1


def submit():
    for i in user_info:
        print(user_info[i].get())


submit_button = ttk.Button(win, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2)

win.mainloop()