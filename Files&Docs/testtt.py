
import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")
console.resizable(False, False)
console.columnconfigure(0, weight=1)
console.rowconfigure(0, weight=1)
console.rowconfigure(1, weight=1)

# def showAndHide(visiable):
#     for i in (settings, menu, startGame):
#         i.pack_forget()
#     visiable.pack(fill="both", expand= True)

menu = tk.Frame(console, bg= "Green")
startGame = tk.Frame(console, bg = "Lightblue")
settings = tk.Frame(console, bg = "Gray")

class Buttons:
    def __init__(self,  place, text, width, height):
        def showAndHide(visiable):
            for i in (settings, menu, startGame):
                i.pack_forget()
            visiable.pack(fill="both", expand= True)
        self.text = text
        self.width = width
        self.height = height
        tk.Button(place, text, width, height)
        

class Package:
    def __init__(self):
        self.pady = 5
        self.padx = 5


start = Buttons(menu, "Start the game", 15, 2)

sett = tk.Button(Buttons(menu, "Settings", 15, 2, command=lambda: showAndHide(settings))).pack(Package())
score = tk.Button(Buttons(menu, "Scoreboard", 15, 2, None)).pack(Package())


menu.pack()
console.mainloop()
