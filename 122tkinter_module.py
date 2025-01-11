from cgitb import text
from re import S
import tkinter


# python tkinter tutorial 
# tee-kinter, tk-inter, kinter

#started code
# import tkinter
import tkinter as tk
# from tkinter import *    # all is imported from tkinter
# window = Tk()         # can be given any name mostly preffered window, or root

from tkinter import Button, ttk
from turtle import width     # it's a subclass of tkinter having nice widgets, ttk labels are beatuiful than tk, we can use tk instead of ttk as well

from csv import DictWriter
import os

win = tk.Tk()
win.title("GUI")


# adding widgets to our GUI window 
# create labels 
# 1. 
# ttk.Label(win, text="Enter you name : ").pack()   # will be at centre
# 2. 
# ttk.Label(win, text="Enter you name : ").grid(row=0, column=0)
name_label = ttk.Label(win, text="Enter your name : ")    # ttk module main label name class hain, name_label is the instance of that class
name_label.grid(row=0, column=0, sticky=tk.W)       # sticky will helps to stick on the west direction 

age_label = ttk.Label(win, text="Enter your age : ")
age_label.grid(row=2, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="Enter your email : ")
email_label.grid(row=1, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Select Gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)


# create entry box 
name_var = tk.StringVar()     # to store the entry of name
name_entrybox = ttk.Entry(win, width= 16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()     # to store the entry of name
email_entrybox = ttk.Entry(win, width= 16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.IntVar()     # to store the entry of name
age_entrybox = ttk.Entry(win, width= 16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# creating a combobox 
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')  # to only read value of combobox not to write
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)      # by default 0th index value is selected 
gender_combobox.grid(row=3, column=1)

# create a radio buttons
profession_var = tk.StringVar()
professio_radiobtn = ttk.Radiobutton(win, text='sutdent', value='student', variable=profession_var ) # textvariable won't work
professio_radiobtn.grid(row=4, column=0)

# profession_var = tk.StringVar()  # creating a new variable is useless coz it will take both the profession at a time
professio_radiobtn = ttk.Radiobutton(win, text='teacher', value='teacher', variable=profession_var )
professio_radiobtn.grid(row=4, column=1)

# creating a check btn 
check_var = tk.IntVar() # if chekced then 0, uncheck then 1
check_btn = ttk.Checkbutton(win, text='check for subscribtion and newletter', variable=check_var )
check_btn.grid(row=5, columnspan=3)




# create a button 
# crating a command for a button 
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    print(f"{username} is {userage} yrs old, {useremail}")
    usergender = gender_var.get()
    userprofession = profession_var.get()
    if check_var.get() == 0:
        subscribed = 'didn\'n Subscribe'
    else :
        subscribed = 'Subscribed'
    print(f"{usergender} {userprofession} {subscribed}")

    # to write the data in the .txt file
    with open ('122tkinter_demo.txt', 'a') as f:
        f.write(f"{username}, {userage}, {useremail}, {usergender}, {subscribed}, {userprofession} \n")

    # to delete the data written in the below boxes when hit submit button
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)

    # changing the color 
    name_label.config(foreground="#aaaeee")   # any hexa value can be taken
    age_label.config(background='red')

    # submit_btn.config(foreground='blue')       # since used ttk so it won't change without style change to tk and try 

    # write in a csv file 
    with open ('122tkinter_demo.csv', 'a') as f:
        dict_writer =DictWriter(f, fieldnames=['user name', 'user email', 'user age', 'user gender', 'user profession', 'subscribed'])
        if os.stat('122tkinter_demo.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'user name': username, 
            'user email': useremail, 
            'user age' : userage, 
            'user gender' : usergender, 
            'user profession' : userprofession, 
            'subscribed' : subscribed
        })



    

submit_btn = ttk.Button(win, text='Submit', command=action )
submit_btn.grid(row=6, column=0)






win.mainloop()      # it implies GUI window will be on for infinte time unless you close it maually