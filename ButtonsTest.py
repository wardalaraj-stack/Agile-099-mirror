import tkinter as tk

def Buttons():
    console = tk.Tk()
    console.geometry("300x200")
    console.title("Main menu")

    start = tk.Button(console, text = "Start the game")#at the top 1
    start.pack()
    #-------------------------------------------------------------------
    level = tk.Button(console, text = "Difficulty level") #under start
    level.pack()
    skins = tk.Button(console, text = "Change skin") #under start
    skins.pack()
    #------------------------------------------------------------------
    score = tk.Button(console, text = "Scoreboard") #under in the middle 2
    score.pack()
    
    settings_window = tk.Frame(console)
    
    audio = tk.Button(console, text = "Audio")
    audio.pack()
    if settings_window.winfo_ismapped():
        settings_window.pack_forget()
    
        pass
    settings = tk.Button(console, text = "Settings") #at the bottom 3
    settings.pack()

    end = tk.Button(console, text = "Close the game", command = console.destroy)#at the veery bottom  4
    end.pack()



    console.mainloop()

Buttons()