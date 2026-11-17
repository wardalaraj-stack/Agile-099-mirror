import tkinter as tk

def Buttons():
    root = tk.Tk()

    menu = tk.Button(root, text = "Menu")
    menu.pack()

    start = tk.Button(root, text = "Start the game")
    start.pack()

    end = tk.Button(root, text = "Close the game", command = root.destroy)
    end.pack()
    root.mainloop()

Buttons()