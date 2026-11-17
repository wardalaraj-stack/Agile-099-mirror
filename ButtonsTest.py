import tkinter as tk
from tkinter import *
from tkinter.ttk import *




def Buttons():
    # def openSettings():
    #     settingWindow = Toplevel(console)   
         
    #     Label(settingWindow, text="This is a new window").pack(pady=20)  

    # def welcome():
    #     print("Welcome to the game")

    console = tk.Tk()
    console.geometry("300x200")
    console.title("Main menu")

    #-----------------
    mainMenu_frame = tk.Frame(console).pack()
    #mainMenu_frame.title("New menu")

    settings_frame = tk.Frame(mainMenu_frame)
    start_frame = tk.Frame(mainMenu_frame)
    
    def changeToSettings():
        settings_frame.pack(fill="both", expand= 1)
        mainMenu_frame.forget()
        start_frame.forget()
        #console.forget()
        

    def changeToStart():
        start_frame.pack(fill = 'both', expand = 1)
        mainMenu_frame.forget()
        settings_frame.forget()


    def changeToMenu():
        start_frame.forget()
        mainMenu_frame.pack(fill = 'both', expand = 1)
        settings_frame.forget()    
    #------------------
    start = tk.Button(mainMenu_frame, text = "Start the game", command=changeToStart).pack() #at the top 1
    #-------------------------------------------------------------------
    level = tk.Button(start_frame, text = "Difficulty level").pack() #under start
    skins = tk.Button(start_frame, text = "Change skin").pack() #under start
    #skins
    #------------------------------------------------------------------
    score = tk.Button(mainMenu_frame, text = "Scoreboard").pack() #under in the middle 2
    #dummy = Toplevel(console)    
    #Label(dummy, text="This is a new window").pack(pady=20)
    
    #settings_window = tk.Frame(console)
    settings = tk.Button(mainMenu_frame, text = "Settings", command=changeToSettings).pack() #at the bottom 3

    audio = tk.Button(settings_frame, text = "Audio").pack()

    back = tk.Button(mainMenu_frame, text = "Back to menu", command = changeToMenu).pack()
    end = tk.Button(console, text = "Close the game", command = console.destroy).pack() #at the veery bottom  4


    console.mainloop()

Buttons()


class MainMenu:
    def Main(self, master):
            mainMenu_frame = tk.Frame(master)
            mainMenu_frame.pack(fill = 'both', expand = 1)
            

