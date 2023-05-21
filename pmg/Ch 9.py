#01
from tkinter import *

window = Tk()
window.title = "Welcome"

def clicked():
    l['text'] = "Clicked"

l = Label(window,text="Hi!")
l.grid(column=0, row=0)
b = Button(window,text="click me",command=clicked)
b.grid(column=1,row=0)

window.mainloop()


#02.
from tkinter import *

window=Tk()
window.title("Welcome to tkinter")
l = Label(window,width=50,height=3,bg="orange",fg="blue",text="Hello, I'm Label")
l.pack()

window.mainloop()


#04
from tkinter import *

window = Tk()

Label(window,text="이름:").grid(row=0)
Label(window,text="주소:").grid(row=1)
Label(window,text="도:").grid(row=2)
Label(window,text="우편번호:").grid(row=3)
Label(window,text="국가:").grid(row=4)

Entry(window).grid(row=0,column=1,columnspan=2)
Entry(window).grid(row=1,column=1,columnspan=2)
Entry(window).grid(row=2,column=1,columnspan=2)
Entry(window).grid(row=3,column=1,columnspan=2)
Entry(window).grid(row=4,column=1,columnspan=2)

Button(window,text='Clear').grid(row=5,column=1)
Button(window,text='Submit').grid(row=5,column=2)
window.mainloop()


#09.
from tkinter import *

window = Tk()

Label(window,text='이름').grid(row=0,column=0,columnspan=2)
Label(window,text='직업').grid(row=1,column=0,columnspan=2)
Label(window,text='국적').grid(row=2,column=0,columnspan=2)

Entry(window).grid(row=0,column=2)
Entry(window).grid(row=1,column=2)
Entry(window).grid(row=2,column=2)

Button(window,text='Show').grid(row=3,column=0)
Button(window,text='Quit').grid(row=3,column=1)

window.mainloop()


#13.
from tkinter import *

window = Tk()
frame = Frame(window, width=500, height=300)

def left(event):
    canvas.move(id, -10, 0)

def right(event):
    canvas.move(id, 10, 0)

def down(event):
    canvas.move(id, 0, 10)

def up(event):
    canvas.move(id, 0, -10)


frame.bind('<Left>', left)
frame.bind('<Right>', right)
frame.bind('<Up>', up)
frame.bind('<Down>', down)
frame.focus_set()
frame.pack()

canvas = Canvas(frame, bg = "white", width = 500, height = 300)
canvas.grid(row=0, column=0, columnspan=4)
id = canvas.create_rectangle(10,150,50,200, fill = "green")

window.mainloop()
