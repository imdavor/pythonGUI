from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


# Create a Function
def speak():
    my_label.config(text=f"You typed: {my_entry.get()}")


# Create Entry Widget
my_entry = tb.Entry(
    root,
    bootstyle="success",
    font=("Helvetica, 18"),
    foreground="white",  # show="*"
)
my_entry.pack(pady=20)

# Create a button
my_button = tb.Button(root, text="Click Me", bootstyle="danger outline", command=speak)
my_button.pack(pady=10)

# Create a label
my_label = tb.Label(root, bootstyle="success", font=("Helvetica, 18"))
my_label.pack(pady=10)


root.mainloop()
