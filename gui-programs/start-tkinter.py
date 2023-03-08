
from tkinter import *


window=Tk()
window.title("first gui program")
window.minsize(width=500,height=300)


my_label=Label(text="I am a label",font=("arial",24,"bold"))
my_label.pack()

my_label["text"]="new label"
my_label.config(text="new label")

def button_clicked():
    #print("ı got clicked")
    #my_label.config(text="button got clicked")
    my_label.config(text=input.get())

button=Button(text="click",command=button_clicked)
button.pack()


input=Entry(width="55")
input.pack()
print(input.get())



 
window.mainloop()