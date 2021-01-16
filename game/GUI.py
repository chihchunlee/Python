from tkinter import *

window = Tk()
window.title('my first GUI')

def hello_function():
    print('Hello,World')
    display_area.config(text="Hello,World",fg="yellow",bg="black")

bytton1 = Button(window, text="Click Me",command = hello_function)
bytton1.pack()

display_area = Label(window,text="")
display_area.pack()

window.mainloop()