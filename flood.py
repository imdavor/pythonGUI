from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


my_gauge = tb.Floodgauge(
    root,
    bootstyle="success",
    font=("Helvetica", 18),
    mask="Pos: {}%",
    maximum=100,
    orient="horizontal",
    value=0,
    mode="determinate",
)
my_gauge.pack(pady=20, fill=X, padx=20)


# Functions
def starter():
    my_gauge.start()


def stopper():
    my_gauge.stop()


def incrementer():
    my_gauge.step(10)
    my_label.config(text=f"Position: {my_gauge.variable.get()}")


def decrementer():
    my_gauge.step(-10)
    my_label.config(text=f"Position: {my_gauge.variable.get()}")


# Buttons
start_button = tb.Button(
    root, text="Start", bootstyle="danger outline", command=starter
)
start_button.pack(pady=5)

stop_button = tb.Button(root, text="Stop", bootstyle="danger outline", command=stopper)
stop_button.pack(pady=5)

increment_button = tb.Button(
    root, text="Increment", bootstyle="danger outline", command=incrementer
)
increment_button.pack(pady=5)

decrement_button = tb.Button(
    root, text="Decrement", bootstyle="danger outline", command=decrementer
)
decrement_button.pack(pady=5)

# Labels
my_label = tb.Label(root, text="Position")
my_label.pack(pady=5)


root.mainloop()
