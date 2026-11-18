"""Grid coordinates and boundary checks for the Snake map."""


class MapGrid:
    """A rectangular grid of zero-based (column, row) positions."""

    def __init__(self, width, height):
        """Save the number of columns and rows after validating them."""
        # A grid needs a positive whole number of columns and rows.
        if type(width) is not int or type(height) is not int:
            raise TypeError("Grid dimensions must be integers.")
        if width <= 0 or height <= 0:
            raise ValueError("Grid dimensions must be positive.")
        self.width = width
        self.height = height

    def cells(self):
        """Yield each cell once, moving left to right and then down."""
        # Finish one row before starting the next. Counting starts at zero.
        for row in range(self.height):
            for column in range(self.width):
                yield column, row

    def contains(self, position):
        """Return whether position belongs to the grid, including its corners."""
        crossed_edges = self.outside_edges(position)
        # An empty result means the position is inside the grid.
        return not crossed_edges

    def outside_edges(self, position):
        """Return crossed sides for an integer position, horizontal side first."""
        column, row = position
        if type(column) is not int or type(row) is not int:
            raise TypeError("A cell position must contain two integers.")

        edges = []
        # Check the column for left or right.
        if column < 0:
            edges.append("left")
        elif column >= self.width:
            edges.append("right")

        # Check the row separately because a position can cross two edges.
        if row < 0:
            edges.append("top")
        elif row >= self.height:
            edges.append("bottom")

        # Return a tuple such as ("right",) or () for a position inside.
        return tuple(edges)
