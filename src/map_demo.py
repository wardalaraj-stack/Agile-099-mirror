"""Show the map, its outer frame, and a test marker controlled by arrows."""

from .map_grid import MapGrid


CELL_SIZE = 46
MARGIN = 14
TILE_COLORS = ("#d8f0e2", "#c5e6d4")
BORDER_COLOR = "#17674e"
MARKER_COLOR = "#245b95"
# Every arrow gives a change to the column and a change to the row.
DIRECTIONS = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1),
}


def cell_box(position):
    """Translate a grid position to a rectangle measured in pixels."""
    column, row = position
    # Add the margin so that the grid does not start at the window border.
    left = MARGIN + column * CELL_SIZE
    top = MARGIN + row * CELL_SIZE
    right = left + CELL_SIZE
    bottom = top + CELL_SIZE
    return left, top, right, bottom


def draw_map(canvas, grid):
    """Draw every cell and one visible frame around the grid."""
    for column, row in grid.cells():
        left, top, right, bottom = cell_box((column, row))
        # The remainder alternates between 0 and 1 for neighboring cells.
        color_index = (column + row) % 2
        tile_color = TILE_COLORS[color_index]
        canvas.create_rectangle(
            left, top, right, bottom,
            fill=tile_color,
            outline="",
            tags="cell",
        )

    # Draw the outer frame after the cells so the edge remains visible.
    frame_right = MARGIN + grid.width * CELL_SIZE
    frame_bottom = MARGIN + grid.height * CELL_SIZE
    canvas.create_rectangle(
        MARGIN, MARGIN, frame_right, frame_bottom,
        outline=BORDER_COLOR,
        width=3,
        tags="outer_frame",
    )


def next_position(grid, current, step):
    """Move the demo marker by one step, keeping it inside the frame."""
    column, row = current
    column_step, row_step = step
    next_column = column + column_step
    next_row = row + row_step
    candidate = (next_column, next_row)

    crossed_edges = grid.outside_edges(candidate)
    if crossed_edges:
        # Keep the last valid position and report the crossed edges.
        return current, crossed_edges
    return candidate, ()


def main():
    """Open the demo window, draw the map, and listen for arrow keys."""
    # Import Tk only when opening the window. The grid tests can run without it.
    import tkinter as tk

    grid = MapGrid(width=8, height=5)
    position = (0, 0)

    window = tk.Tk()
    window.title("Snake | Grid and outer edges")
    window.resizable(False, False)

    tk.Label(window, text="Arrow keys: move the blue marker").pack(pady=(10, 2))
    canvas = tk.Canvas(
        window,
        width=grid.width * CELL_SIZE + 2 * MARGIN,
        height=grid.height * CELL_SIZE + 2 * MARGIN,
        highlightthickness=0,
        background="#f4f8f6",
    )
    canvas.pack()
    draw_map(canvas, grid)
    marker = canvas.create_oval(0, 0, 0, 0, fill=MARKER_COLOR, outline="")
    status = tk.Label(window, anchor="w", width=44)
    status.pack(padx=MARGIN, pady=(2, 10))

    def show_marker():
        """Move the blue marker to the current cell with a small inset."""
        left, top, right, bottom = cell_box(position)
        canvas.coords(marker, left + 10, top + 10, right - 10, bottom - 10)

    def on_key(event):
        """Apply an arrow key and refresh the marker and status message."""
        # Update the position stored in main so the next key starts there.
        nonlocal position
        step = DIRECTIONS[event.keysym]
        position, crossed_edges = next_position(grid, position, step)
        show_marker()
        if crossed_edges:
            edge_names = ", ".join(crossed_edges)
            status.config(text=f"Crossed: {edge_names}. Marker stays {position}.")
        else:
            status.config(text=f"Position (column, row): {position}")

    show_marker()
    status.config(text=f"Position (column, row): {position}")
    # Register the handler once for each arrow, then wait for events.
    for key in DIRECTIONS:
        window.bind(f"<{key}>", on_key)
    window.mainloop()


if __name__ == "__main__":
    main()
