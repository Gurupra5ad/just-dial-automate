import tkinter as tk
from tkinter.constants import INSERT
from tkinter import font

HEIGHT = 700
WIDTH = 800

def test(entry):
    # print("The entry is : ", entry)
    label['text'] = "The entry is :" + entry

root = tk.Tk()

root.title("Just-Dial Scraper")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#a58faa")
canvas.pack()

frame = tk.Frame(root, bg="#ededd0",bd=5)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Times", 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, font=("Times", 15), text="Submit", bg="#a58faa", command= lambda: test(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#ededd0",bd=10)
lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5,anchor="n")

label = tk.Label(lower_frame, font=("Times", 30))
label.place(relwidth=1, relheigh=1)
root.mainloop()

