"""Show the map, its outer frame, and a test marker controlled by arrows."""

from board import Board


CELL_SIZE = 46
MARGIN = 14
TILE_COLORS = ("#d8f0e2", "#c5e6d4")
BORDER_COLOR = "#17674e"
MARKER_COLOR = "#245b95"
DIRECTIONS = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1),
}


def cell_box(position):
    """Translate a grid position to a rectangle measured in pixels."""
    column, row = position
    left = MARGIN + column * CELL_SIZE
    top = MARGIN + row * CELL_SIZE
    return left, top, left + CELL_SIZE, top + CELL_SIZE


def draw_map(canvas, grid):
    """Draw every cell and one visible frame around the grid."""
    for column, row in grid.cells():
        canvas.create_rectangle(
            *cell_box((column, row)),
            fill=TILE_COLORS[(column + row) % 2],
            outline="",
            tags="cell",
        )

    canvas.create_rectangle(
        MARGIN,
        MARGIN,
        MARGIN + grid.width * CELL_SIZE,
        MARGIN + grid.height * CELL_SIZE,
        outline=BORDER_COLOR,
        width=3,
        tags="outer_frame",
    )


def next_position(grid, current, step):
    """Move the demo marker by one step, keeping it inside the frame."""
    column, row = current
    column_step, row_step = step
    candidate = column + column_step, row + row_step
    edges = grid.outside_edges(candidate)
    if edges:
        return current, edges
    return candidate, ()


def main():
    import tkinter as tk

    grid = Board(width=8, height=5)
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
        left, top, right, bottom = cell_box(position)
        canvas.coords(marker, left + 10, top + 10, right - 10, bottom - 10)

    def on_key(event):
        nonlocal position
        position, edges = next_position(grid, position, DIRECTIONS[event.keysym])
        show_marker()
        if edges:
            status.config(text=f"Crossed: {', '.join(edges)}. Marker stays {position}.")
        else:
            status.config(text=f"Position (column, row): {position}")

    show_marker()
    status.config(text=f"Position (column, row): {position}")
    for key in DIRECTIONS:
        window.bind(f"<{key}>", on_key)
    window.mainloop()


if __name__ == "__main__":
    main()