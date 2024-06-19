from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")

# Functions


# Labels


# Widget
my_date = tb.DateEntry(root, bootstyle="info")
my_date.pack(pady=20)

# Button
my_button = tb.Button(root, text="Get date", bootstyle="danger outline")
my_button.pack(pady=20)

my_label = tb.Label(root, text="You picked: ")
my_label.pack(pady=10)

root.mainloop()
