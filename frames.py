from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


def click():
    pass

my_frame = tb.Frame(root, bootstyle="warning")
my_frame.pack(pady=20)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=10, padx=10)

my_button = tb.Button(my_frame, text="Click Me", bootstyle="dark", command=click)
my_button.pack(pady=10)

my_label=tb.Label(root, text="Hello There", font=("Helvetica", 18),bootstyle="inverse light")
my_label.pack(pady=10)


root.mainloop()
