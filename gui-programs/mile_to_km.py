import tkinter as tk

def convert():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_label.config(text=f"{km:.2f} km")

root = tk.Tk()
root.title("Mile to Kilometer Converter")

miles_label = tk.Label(root, text="Miles:")
miles_label.pack()

miles_input = tk.Entry(root)
miles_input.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

km_label = tk.Label(root, text="")
km_label.pack()

root.mainloop()
