from src import menu, board_launch


def main():
    # Monkey patching!
    board_launch.main = lambda: None

    menu.main()


if __name__ == "__main__":
    main()
