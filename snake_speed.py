
class SnakeSpeed:
    # speed should be the number of cells we want to move in a second
    def __init__(self, speed):
        self.interval = 1 / speed
        self.timepassed = 0.0

    def update(self, dt):
        """dt updates the time passed and when it reaches interval the snake should move"""
        self.timepassed += dt

        if self.timepassed >= self.interval:
            self.timepassed -= self.interval
            return True
        else:
            return False    
    