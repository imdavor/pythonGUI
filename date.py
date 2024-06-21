from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap! Date entry")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


# Functions
def datey():
    # grab the date
    my_label.config(text=f"You picked: {my_date.entry.get()}")

def getCalendar():
    cal=Querybox
    my_label.config(text=f"You picked: {cal.get_date()}")

# Widget
my_date = tb.DateEntry(
    root, bootstyle="danger", firstweekday=0, startdate=date(2024, 6, 21)
)
my_date.pack(pady=20)

# Button
my_button = tb.Button(root, text="Get date", bootstyle="danger outline", command=datey)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Get calendar", bootstyle="success outline", command=getCalendar)
my_button2.pack(pady=20)

my_label = tb.Label(root, text="You picked: ")
my_label.pack(pady=10)

root.mainloop()
