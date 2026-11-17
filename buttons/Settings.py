import tkinter as tk

console = tk.Tk()
console.geometry("300x200")
console.title("Main menu")

settings = tk.Frame(console)


audio = tk.Button(settings, text = "Audio settings") #to start frame
audio.pack()

goBack = tk.Button(settings, text="Back to Main menu")#command to MM
goBack.pack()


settings.pack()
console.mainloop()