from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")

def stuff(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=f'You selected: {x}')


my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=50)

# create basic menu
inside_menu = tb.Menu(my_menu)
# add items inside Menu
item_var = StringVar()
for x in [
    "primary",
    "secondary",
    "danger",
    "info",
    "outline primary",
    "outline secondary",
    "outline danger",
    "outline info",
]:
    inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

# associate inside menu with menu button
my_menu["menu"] = inside_menu

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=50)

root.mainloop()
