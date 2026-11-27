import tkinter as tk
from tkinter import ttk
from src import board_launch, scoreboardfile


def main():
    root = tk.Tk()

    width = 640
    height = 400

    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

    root.title("Main menu")
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    def show_frame(target_frame):
        for frame in (settings_frame, main_menu_frame, start_game_frame, scoreboard_frame):
            frame.place_forget()
        target_frame.place(relx=0.5, rely=0.5, anchor="center")

    def start_game():
        board_launch.main()

    main_menu_frame = tk.Frame(root, bg="Green")
    main_menu_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Main Menu
    start_button = tk.Button(
        main_menu_frame,
        text="Start the game",
        command=lambda: show_frame(start_game_frame),
        width=15,
        height=2
    )
    start_button.pack(pady=5, padx=5)

    settings_button = tk.Button(
        main_menu_frame,
        text="Settings",
        command=lambda: show_frame(settings_frame),
        width=15,
        height=2
    )
    settings_button.pack(pady=5, padx=5)

    scoreboard_button = tk.Button(
        main_menu_frame,
        text="Scoreboard",
        command=lambda: show_frame(scoreboard_frame),
        width=15,
        height=2
    )
    scoreboard_button.pack(pady=5, padx=5)

    quit_button = tk.Button(
        main_menu_frame,
        text="Close the game",
        command=root.destroy,
        width=15,
        height=2
    )
    quit_button.pack(pady=5, padx=5)

    # Start the game
    start_game_frame = tk.Frame(root, bg="Lightblue")

    play_button = tk.Button(
        start_game_frame,
        text="Play",
        command=lambda: start_game(),
        width=15,
        height=2
    )
    play_button.pack(pady=5, padx=5)

    difficulty_button = tk.Button(
        start_game_frame,
        text="Difficulty level",
        width=15,
        height=2
    )
    difficulty_button.pack(pady=5, padx=5)

    skin_button = tk.Button(
        start_game_frame,
        text="Change skin",
        width=15,
        height=2
    )
    skin_button.pack(pady=5, padx=5)

    back_button = tk.Button(
        start_game_frame,
        text="Back to Main menu",
        command=lambda: show_frame(main_menu_frame),
        width=15,
        height=2
    )
    back_button.pack(pady=5, padx=5)

    # Settings
    settings_frame = tk.Frame(root, bg="Gray")

    audio_button = tk.Button(
        settings_frame,
        text="Audio",
        width=15,
        height=2
    )
    audio_button.pack(pady=5, padx=5)


    back_button = tk.Button(
        settings_frame,
        text="Back to Main menu",
        command=lambda: show_frame(main_menu_frame),
        width=15,
        height=2
    )
    back_button.pack(pady=5, padx=5)

#scoreboard
    scoreboard_frame = tk.Frame(root, bg="Yellow")

    score_table = ttk.Treeview(
        scoreboard_frame,
        columns=("place", "player", "score"),
        show="headings",
        height=5,
    )
    score_table.heading('place', text = 'Place')
    score_table.heading('player', text = 'Player')
    score_table.heading('score', text = 'Score')

    score_table.column("place", width=80, anchor="center")
    score_table.column("player", width=100)
    score_table.column("score", width=80, anchor="e")

   # for place in scoreboard_frame:
    #    score_table.insert('')


    score_table.pack(padx=12, pady=12)


    back_button = tk.Button(
        scoreboard_frame,
        text="Back to Main menu",
        command=lambda: show_frame(main_menu_frame),
        width=15,
        height=2
    )
    back_button.pack(pady=5, padx=5)
    root.mainloop()
