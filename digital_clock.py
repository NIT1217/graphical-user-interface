import tkinter as tk
import time
root = tk.Tk()

root.title("digital clock")

def  update_time():
    label.config(text = time.strftime("%H:%M:%S\n%A-%B-%Y"))
    label.after(1000,update_time)

label = tk.Label(root,font=("calibri",30,"bold"),bg = "black",fg = "white")

label.pack()

update_time()
root.mainloop()


