import tkinter


window=tkinter.Tk()
window.title("first gui program")
window.minsize(width=500,height=300)


my_label=tkinter.Label(text="I am a label",font=("arial",24,"bold"))
my_label.pack()


window.mainloop()