from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Boostrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Style - make button bigger
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))

my_button = tb.Button(
    text="Hello World",
    bootstyle="success",
    style="success.Outline.TButton")
my_button.pack(pady=50)

root.mainloop()
