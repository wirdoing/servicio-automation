import tkinter as tk

root = tk.Tk()
root.withdraw()
c = root.clipboard_get()
print(c)