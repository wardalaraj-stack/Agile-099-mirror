import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")

startGame = tk.Frame(console)


start = tk.Button(startGame, text = "Start the game") #activate the game
start.pack()
lvl = tk.Button(startGame, text = "Difficulty level")
lvl.pack()
skins = tk.Button(startGame, text = "Change skin")
skins.pack()
goBack = tk.Button(startGame, text="Back to Main menu")#command to MM
goBack.pack()

startGame.pack()
console.mainloop()