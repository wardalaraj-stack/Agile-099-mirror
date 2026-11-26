import tkinter as tk
from src import board_launch


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
        for frame in (settings_frame, main_menu_frame, start_game_frame):
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

    root.mainloop()
