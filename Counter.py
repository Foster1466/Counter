from tkinter import *


def increment():
    root.counter += 1
    lblCount['text'] = str(root.counter)


def decrement():
    if root.counter > 0:
        root.counter -= 1
    lblCount['text'] = str(root.counter)


def reset():
    root.counter = 0
    lblCount['text'] = str(root.counter)


def start_value():
    root.withdraw()
    sv.deiconify()
    sv_entry.delete(0,END)
    sv_entry.focus()

def set():
    val= sv_entry.get()
    root.counter = int(val)
    lblCount['text'] = str(root.counter)
    sv.withdraw()
    root.deiconify()


root = Tk()
root.counter = 0
root.title("Counter")
root.iconbitmap(r'icon.ico')
root.maxsize(450, 230)
root.geometry("450x230+400+100")
root.resizable(width=False, height=False)
root.configure(background='gray94')

lblCount = Label(root, text='0', font=('courier', 40, 'bold italic'))
btnIncrement = Button(root, text="+", width=15, font=('Corbel Light', 18), command=increment)
btnDecrement = Button(root, text="-", width=15, font=('Corbel Light', 18), command=decrement)
btnReset = Button(root, text="Reset", width=15, font=('Corbel Light', 18), command=reset)
btnStartvalue = Button(root, text="Start value", width=15, font=('Corbel Light', 18), command=start_value)

lblCount.pack()
btnIncrement.place(x=240, y=100)
btnDecrement.place(x=20, y=100)
btnReset.place(x=20, y=160)
btnStartvalue.place(x=240, y=160)

sv= Toplevel(root)
sv.title("Start value")
sv.geometry("250x130+600+300")

sv_entry= Entry(sv, width= 15, bd = 2, font = ('Yu Gothic Light', 18))
sv_button= Button(sv,width= 10, text = "Set", font = ('Corbel Light', 18), command = set)

sv_entry.pack()
sv_button.pack(pady= 15)
sv.withdraw()

root.mainloop()
