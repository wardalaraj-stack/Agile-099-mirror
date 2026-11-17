import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")

def changeToSettings():
        settings.pack(fill="both", expand= 1)
        menu.forget()
        startGame.forget()
        #console.forget()

def changeToStart():
        settings.forget()
        menu.forget()
        startGame.pack(fill="both", expand= 1)

def changeToMenu():
        settings.forget()
        menu.pack(fill="both", expand= 1)
        startGame.forget()

menu = tk.Frame(console)


start = tk.Button(menu, text = "Start the game", command = changeToStart) #to start frame
start.pack()
sett = tk.Button(menu, text = "Settings", command = changeToSettings)#to sett frame
sett.pack()
end = tk.Button(menu, text = "Close the game", command = console.destroy)
end.pack()

menu.pack()
#-----------------
startGame = tk.Frame(console)


start = tk.Button(startGame, text = "Start the game") #activate the game
start.pack()
lvl = tk.Button(startGame, text = "Difficulty level")
lvl.pack()
skins = tk.Button(startGame, text = "Change skin")
skins.pack()
goBack = tk.Button(startGame, text="Back to Main menu", command = changeToMenu)#command to MM
goBack.pack()

#startGame.pack()
#-----------------------
settings = tk.Frame(console)


audio = tk.Button(settings, text = "Audio") #to start frame
audio.pack()

goBack = tk.Button(settings, text="Back to Main menu", command = changeToMenu)#command to MM
goBack.pack()
   

console.mainloop()