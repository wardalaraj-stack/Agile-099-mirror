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

#-----------Main Menu--------------
start = tk.Button(menu, text = "Start the game", command=lambda: showAndHide(startGame))
start.pack()
sett = tk.Button(menu, text = "Settings", command = lambda: showAndHide(settings))
sett.pack()
score = tk.Button(menu, text = "Scoreboard")
score.pack()
end = tk.Button(menu, text = "Close the game", command = console.destroy)
end.pack()

menu.pack()

#--------Start the game---------
startGame = tk.Frame(console, bg = "Lightblue")


start = tk.Button(startGame, text = "Play")
start.pack()
lvl = tk.Button(startGame, text = "Difficulty level")
lvl.pack()
skins = tk.Button(startGame, text = "Change skin")
skins.pack()
goBack = tk.Button(startGame, text="Back to Main menu", command = lambda: showAndHide(menu))
goBack.pack()

#----------Settings-------------
settings = tk.Frame(console, bg = "Gray")


audio = tk.Button(settings, text = "Audio", width=15, height=2)
audio.pack(pady = 5, padx = 5)

goBack = tk.Button(settings, text="Back to Main menu", command = lambda: showAndHide(menu), width=15, height=2)
goBack.pack(pady = 5, padx = 5)
   

console.mainloop()