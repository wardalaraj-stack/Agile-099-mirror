import pygame

# Background and grid_color are red, green, and blue color values.
BACKGROUND_COLOR = (15, 43, 92)
GRID_COLOR = (255, 153, 235)


class BoardView:
    """Pygame drawing adapter; the Board itself does not depend on pygame."""

    def __init__(
        self,
        board,
        offset=(0, 0),
        background=BACKGROUND_COLOR,
        grid_color=GRID_COLOR
    ):
        self.board = board

        # Offset is the board's distance from the window's top-left corner.
        self.offset = offset
        self.background = background
        self.grid_color = grid_color

    @property
    def pixel_size(self):
        # Give the board's width and height in screen pixels, not cells.
        return (
            self.board.width * self.board.cell_size,
            self.board.height * self.board.cell_size,
        )

    def cell_rect(self, position):
        # Convert a cell's (column, row) position into a pygame rectangle.
        x, y = position
        offset_x, offset_y = self.offset
        cell_size = self.board.cell_size

        return pygame.Rect(
            offset_x + x * cell_size,
            offset_y + y * cell_size,
            cell_size, cell_size
        )

    def draw_cell(self, surface, position, color, inset=1):
        # Draw one cell on a surface, leaving an inset gap around its edges.
        rect = self.cell_rect(position)
        rect = rect.inflate(-2 * inset, -2 * inset)
        pygame.draw.rect(surface, color, rect)

    def draw(self, surface):
        # Draw the background, grid, and visible rule cells on a surface.
        offset_x, offset_y = self.offset
        width, height = self.pixel_size
        pygame.draw.rect(
            surface, self.background,
            pygame.Rect(offset_x, offset_y, width, height)
        )

        # Draw the grid.
        cell_size = self.board.cell_size
        for x in range(self.board.width + 1):
            pixel_x = offset_x + x * cell_size
            pygame.draw.line(
                surface, self.grid_color,
                (pixel_x, offset_y),
                (pixel_x, offset_y + height)
            )

        for y in range(self.board.height + 1):
            pixel_y = offset_y + y * cell_size
            pygame.draw.line(
                surface, self.grid_color,
                (offset_x, pixel_y),
                (offset_x + width, pixel_y)
            )

        # Every rule controls its own visual cells and color.
        for rule in self.board.rules:
            for cell in rule.cells():
                self.draw_cell(surface, cell, rule.color)
