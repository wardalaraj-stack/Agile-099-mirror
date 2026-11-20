import tkinter as tk
import board_launch

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

def gameStart():
    board_launch.main()

menu = tk.Frame(console, bg= "Green")

#-----------Main Menu--------------
start = tk.Button(menu, text = "Start the game", command=lambda: showAndHide(startGame), width=15, height=2)
start.pack(pady = 5, padx = 5)
sett = tk.Button(menu, text = "Settings", command = lambda: showAndHide(settings), width=15, height=2)
sett.pack(pady = 5, padx = 5)
score = tk.Button(menu, text = "Scoreboard", width=15, height=2)
score.pack(pady = 5, padx = 5)
end = tk.Button(menu, text = "Close the game", command = console.destroy, width=15, height=2)
end.pack(pady = 5, padx = 5)

menu.pack()

#--------Start the game---------
startGame = tk.Frame(console, bg = "Lightblue")


start = tk.Button(startGame, text = "Play", command = lambda: gameStart(), width=15, height=2)
start.pack(pady = 5, padx = 5)
lvl = tk.Button(startGame, text = "Difficulty level", width=15, height=2)
lvl.pack(pady = 5, padx = 5)
skins = tk.Button(startGame, text = "Change skin", width=15, height=2)
skins.pack(pady = 5, padx = 5)
goBack = tk.Button(startGame, text="Back to Main menu", command = lambda: showAndHide(menu), width=15, height=2)
goBack.pack(pady = 5, padx = 5)

#----------Settings-------------
settings = tk.Frame(console, bg = "Gray")


audio = tk.Button(settings, text = "Audio", width=15, height=2)
audio.pack(pady = 5, padx = 5)

goBack = tk.Button(settings, text="Back to Main menu", command = lambda: showAndHide(menu), width=15, height=2)
goBack.pack(pady = 5, padx = 5)
   

console.mainloop()