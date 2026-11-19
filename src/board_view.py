import pygame


class BoardView:
    #Pygame drawing adapter; the Board itself does not depend on pygame.

    def __init__(self, board, offset=(0, 0), background=(15, 43, 92),       #change background color here
                 grid_color=(255, 153, 235)):                               #change grid color here 
        
        #Set up how to draw a board.
        #Offset is the board's distance from the window's top-left corner.
        #Background and grid_color are red, green, and blue color values.
        

        self.board = board
        self.offset = offset
        self.background = background
        self.grid_color = grid_color

    @property
    def pixel_size(self):
        #Give the board's width and height in screen pixels, not cells.
        return (
            self.board.width * self.board.cell_size,
            self.board.height * self.board.cell_size,
        )

    def cell_rect(self, position):
        #Convert a cell's (column, row) position into a pygame rectangle.
        x, y = position
        ox, oy = self.offset
        size = self.board.cell_size
        return pygame.Rect(ox + x * size, oy + y * size, size, size)

    def draw_cell(self, surface, position, color, inset=1):
        #Draw one cell on a surface, leaving an inset gap around its edges.
        rect = self.cell_rect(position)
        rect = rect.inflate(-2 * inset, -2 * inset)
        pygame.draw.rect(surface, color, rect)

    def draw(self, surface):
        #Draw the background, grid, and visible rule cells on a surface.
        ox, oy = self.offset
        width, height = self.pixel_size
        pygame.draw.rect(
            surface, self.background,
            pygame.Rect(ox, oy, width, height)
        )

        # Draw the grid.
        size = self.board.cell_size
        for x in range(self.board.width + 1):
            px = ox + x * size
            pygame.draw.line(surface, self.grid_color,(px, oy), (px, oy + height))
        for y in range(self.board.height + 1):
            py = oy + y * size
            pygame.draw.line(surface, self.grid_color,
                             (ox, py), (ox + width, py))

        # Every rule controls its own visual cells and color.
        for rule in self.board.rules:
            for cell in rule.cells():
                self.draw_cell(surface, cell, rule.color)
