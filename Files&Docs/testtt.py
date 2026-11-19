
import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")
console.resizable(False, False)
console.columnconfigure(0, weight=1)
console.rowconfigure(0, weight=1)
console.rowconfigure(1, weight=1)

def showAndHide(visiable):
    for i in (settings, menu, startGame):
        i.pack_forget()
    visiable.pack(fill="both", expand= True)

menu = tk.Frame(console, bg= "Green")
startGame = tk.Frame(console, bg = "Lightblue")
settings = tk.Frame(console, bg = "Gray")

class Buttons:
    def __init__(self, place, text, width, height, command):
        self.place = place
        self.text = text
        self.width = width
        self.height = height
        self.command = command

class Package:
    def __init__(self, pady, padx):
        self.pady = pady
        self.padx = padx


# start = tk.Button(menu, "Start the game", 15, 2)
# start.pack(5,5)

start = tk.Button(Buttons(menu, "Start the game", 15, 2, command=lambda: showAndHide(startGame)))


menu.pack()
console.mainloop()
