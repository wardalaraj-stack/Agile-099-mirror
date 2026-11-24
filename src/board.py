import random


class Board:
    #Pygame-independent board geometry and rule management.

    def __init__(self, width=24, height=18, cell_size=28, rules=(), rng=None):
        #Create a board with a size in cells and a cell size in pixels.
        #Rules identify blocked cells. An optional rng controls random choices.
        #Board dimensions and cell_size must be greater than zero.
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive.")
        if cell_size <= 0:
            raise ValueError("cell_size must be positive.")

        self.width = width
        self.height = height
        self.cell_size = cell_size
        self._rules = list(rules)
        self._rng = rng if rng is not None else random.Random()


    @property
    def rules(self):
        #Return the registered rules as a tuple, which cannot be changed.
        return tuple(self._rules)

    def cells(self):
        #Produce each board position one at a time as a (column, row) pair.
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)
    
    def outside_edges(self, position):
            #Return crossed sides for an integer position, horizontal side first.
            column, row = position
            if type(column) is not int or type(row) is not int:
                raise TypeError("A cell position must contain two integers.")

            edges = []
            if column < 0:
                edges.append("left")
            elif column >= self.width:
                edges.append("right")

            if row < 0:
                edges.append("top")
            elif row >= self.height:
                edges.append("bottom")

            return tuple(edges)
    
    def contains(self, position):
        """Return whether position belongs to the grid, including its corners."""
        return not self.outside_edges(position)

"""
    def free_cell(self, occupied=()):
        
        #Return a randomly chosen available position, or None if there is none.
        #A position is available when it is on the board, is not in occupied,
        #and is not blocked by any registered rule.
    
        occupied = {tuple(cell) for cell in occupied}
        available = [
            cell for cell in self.cells()
            if cell not in occupied and not self.is_blocked(cell)
        ]
        if not available:
            return None
        return self._rng.choice(available)
"""

"""
to be impleminted :

   def add_rule(self, rule):
        #Add a rule that has a blocks(position) method to check a cell.
        if not callable(getattr(rule, "blocks", None)):
            raise TypeError("A board rule must provide blocks(position).")
        self._rules.append(rule)

    def is_blocked(self, position):
        #Return True if any registered rule blocks the given position.
        return any(rule.blocks(position) for rule in self._rules)


"""
