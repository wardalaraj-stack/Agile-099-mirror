import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")

menu = tk.Frame(console)


start = tk.Button(menu, text = "Start the game") #to start frame
start.pack()
sett = tk.Button(menu, text = "Settings")#to sett frame
sett.pack()
end = tk.Button(menu, text = "Close the game", command = console.destroy)
end.pack()

menu.pack()
console.mainloop()