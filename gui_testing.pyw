from tkinter import *
from main import organize
root = Tk()
root.title("Downloads Organizer")

l = Label(root, text="", padx=50).grid(row=0, column=0)
l1 = Label(root, text="", padx=50).grid(row=0, column=2)

ob = Button(root, text="Organize!", command=organize)
ob.grid(row=0, column=1)

root.mainloop()