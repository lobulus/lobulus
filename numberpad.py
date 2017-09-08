
#!/usr/bin/env python3.4
from Tkinter import *
import parser

root = Tk()
root.title('Enter Code')
root.geometry("480x320")

i = 0



def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, END)

def get_variables(num):
    """Gets the user input for keycode and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1



def undo():
    """removes the last entered keycode from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error, press Clear")

def verify():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        # code to verify user from keypad goes here
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

root.columnconfigure(0)
root.columnconfigure(1)
root.columnconfigure(2)
root.columnconfigure(3)
root.columnconfigure(4)

root.rowconfigure(0)
root.rowconfigure(1)
root.rowconfigure(2)
root.rowconfigure(3)

display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 3  , sticky = W+E)

one = Button(root, text = "1", width = 4, command = lambda : get_variables(1), font=("Calibri", 35))
one.grid(row = 2, column = 0)
two = Button(root, text = "2", width = 4, command = lambda : get_variables(2), font=("Calibri", 35))
two.grid(row = 2, column = 1)
three = Button(root, text = "3", width = 4, command = lambda : get_variables(3), font=("Calibri",35))
three.grid(row = 2, column = 2)

four = Button(root, text = "4", width = 4, command = lambda : get_variables(4), font=("Calibri",35))
four.grid(row = 3 , column = 0)
five = Button(root, text = "5", width = 4, command = lambda : get_variables(5), font=("Calibri", 35))
five.grid(row = 3, column = 1)
six = Button(root, text = "6", width = 4, command = lambda : get_variables(6), font=("Calibri", 35))
six.grid(row = 3, column = 2)

seven = Button(root, text = "7", width = 4, command = lambda : get_variables(7), font=("Calibri", 35))
seven.grid(row = 4, column = 0)
eight = Button(root, text = "8", width = 4, command = lambda : get_variables(8), font=("Calibri", 35))
eight.grid(row = 4, column = 1)
nine = Button(root , text = "9", width = 4, command = lambda : get_variables(9), font=("Calibri", 35))
nine.grid(row = 4, column = 2)

cls = Button(root, text = "Clear", width = 4, command = clear_all, font=("Calibri", 35), foreground = "red")
cls.grid(row = 5, column = 0)
zero = Button(root, text = "0", width = 4, command = lambda : get_variables(0), font=("Calibri", 35))
zero.grid(row = 5, column = 1)
result = Button(root, text = "Enter", width = 4, command = verify, font=("Calibri", 35), foreground = "red")
result.grid(row = 5, column = 2)









root.mainloop()
