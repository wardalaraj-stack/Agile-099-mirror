class SnakeSpeed:
    # Speed should be the number of cells we want to move in a second
    def __init__(self, speed=1):
        self.interval = 100 / speed
        self.time_passed = 0

    def update(self, dt):
        """Return whether enough time has passed for the snake to move."""
        self.time_passed += dt

        if self.time_passed >= self.interval:
            self.time_passed -= self.interval
            return True
        else:
            return False
