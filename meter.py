from tkinter import *
import ttkbootstrap as tb
from PIL import Image

Image.CUBIC = Image.BICUBIC

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Boostrap! Meter")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")

my_meter = tb.Meter(
    root,
    bootstyle="danger",
    subtext="Tkinter Learned",
    subtextfont=("Helvetica", 14),
    interactive=True,
    textright="$",
    stripethickness=10,
)
my_meter.pack(pady=50)

root.mainloop()
