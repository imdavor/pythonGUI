from tkinter import *
import ttkbootstrap as tb
from PIL import Image

Image.CUBIC = Image.BICUBIC

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Boostrap! Meter")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


def up():
    my_meter.step(10)


def down():
    my_meter.step(-10)


global counter
counter = 5


def clicker():
    global counter
    my_meter.configure(amountused=counter)
    counter += 5
    my_button.configure(text=f'Click Me {my_meter.amountusedvar.get()}')


my_meter = tb.Meter(
    root,
    bootstyle="danger",
    subtext="Tkinter Learned",
    subtextfont=("Helvetica", 14),
    interactive=True,
    textright="%",
    stripethickness=10,
    subtextstyle="danger"
)
my_meter.pack(pady=10)

my_button = tb.Button(root, text="My Button", command=clicker)
my_button.pack(pady=5)

my_buttonUp = tb.Button(root, text="Step Up", command=up)
my_buttonUp.pack(pady=5)

my_buttonDown = tb.Button(root, text="Step Down", command=down)
my_buttonDown.pack(pady=5)

root.mainloop()
