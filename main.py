from tkinter import *

# setting the main window
window = Tk()
window.geometry("400x300")
window.title("main")

# function to open new (top level) window
def topwin():
    # setting up top window
    top = Toplevel()
    top.geometry("100x100")
    top.title("toplevel")
    # adding a label to top window
    l2 = Label(top, text= "This is a toplevel window")
    l2.pack()

    top.mainloop()

# adding a label and button widget to window (Main) window
l = Label(window, text= "This is a root window")
btn = Button(window, text= "Click here to open another window" , command= topwin)

# arranging widgets
l.pack()
btn.pack()

window.mainloop()