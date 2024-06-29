from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
# root = Tk()
root.title("TTK Boostrap! Notebook tabs")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

my_notebook = tb.Notebook(root, style="light")
my_notebook.pack(pady=10)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = Label(tab1, text="My awesome Label 1", font=("Helvetica", 18))
my_label.pack(pady=10)

my_text = Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

my_button = tb.Button(tab1, text="Click Me!", style="danger outline")
my_button.pack(pady=10)

my_label2 = Label(tab2, text="Label number 2", font=("Helvetica", 18))
my_label2.pack(pady=10)

# add frames to notebook
my_notebook.add(tab1, text="Tab 1")
my_notebook.add(tab2, text="Tab 2")

root.mainloop()
