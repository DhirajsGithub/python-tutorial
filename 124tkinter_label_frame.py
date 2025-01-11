import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title("Label Frame")
# idea is to create frames of labels and buttons and other things so that they are packed in a container 

label_frame = tk.LabelFrame(win, text="Information Frame")
label_frame.grid(row=0, column=0, padx=5, pady=5)
# that's or frame in 0,0 row and column
# we will be adding content to this label instead of win
labels = ["your name", "your age", "your email", "your country", "your state", "your city"]
for i in range(len(labels)):
    cur_label = "label" + str(i)
    cur_label = ttk.Label(label_frame, text=("What is your "+ labels[i].split(" ")[1] +" : "))
    # cur_label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
    cur_label.grid(row=i, column=0, sticky=tk.W)


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
    curl_entry = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    # curl_entry.grid(row=counter, column=1, padx=10, pady=5)
    curl_entry.grid(row=counter, column=1)
    counter +=1


def submit():
    for i in user_info:
        print(user_info[i].get())

label_frame2 = tk.LabelFrame(win, text="Button Frame")
label_frame2.grid(row=1, column=0, padx=5, pady=5)
submit_button = ttk.Button(label_frame2, text="Submit")
submit_button.grid(row=0, column=0)



# adding padding to child elemenets of frames 
for child in label_frame.winfo_children():
    child.grid(padx=4, pady=4)



win.mainloop()
