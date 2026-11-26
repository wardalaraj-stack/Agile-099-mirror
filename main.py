import sys


def main():
    if sys.version_info[:2] != (3, 13):
        sys.exit("This project requires Python 3.13. See docs for setup instructions.")

    from src.menu import main as launch_menu
    launch_menu()


if __name__ == "__main__":
    main()
