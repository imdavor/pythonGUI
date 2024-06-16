from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap!")
root.iconbitmap("images/codemy.ico")
root.geometry("500x350")

#Create button click function
def clicker():
    my_label.config(text=f"Odabrali ste {my_combo.get()}!")

#Create binding function - ne moraš klikat već se label promijeni na odabir unutar comba
def click_bind(e):
    my_label.config(text=f"Odabrali ste {my_combo.get()}!")


# Style
my_label = tb.Label(root, text="Hello World", font=("Helvetica", 18))
my_label.pack(pady=30)

# Create dropdown list for combo
days = ["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak", "Subota", "Nedjelja"]

# Create combo box
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=31)

# Make combo default
my_combo.current(0)

# Create a button
my_button = tb.Button(root, text="Button", command=clicker, bootstyle="danger")
my_button.pack(pady=32)
# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
