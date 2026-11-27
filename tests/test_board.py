from tests.setup import setup, run


def main():
    board, view, screen, clock = setup()
    run(view, screen, clock)


if __name__ == "__main__":
    main()
