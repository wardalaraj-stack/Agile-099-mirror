# Pygame Board Marker Design

## Goal

Add the arrow-key-controlled marker demonstrated in `src/map_demo.py` to
`src/board_launch.py` with minimal changes. Keep `src/map_demo.py` and the
existing board configuration and unrelated launcher behavior unchanged.

## Design

Add small module-level helpers in `board_launch.py` to calculate the next
marker cell and draw the marker using the existing `BoardView` cell geometry.
The marker starts at `(0, 0)`, appears as an inset blue ellipse, and moves one
cell for each arrow-key press. A move that would cross the board boundary
leaves the marker in its current cell, matching `map_demo.py`.

Wire the helpers into the existing Pygame loop: handle arrow-key events,
redraw the marker after the board, and retain Escape-to-quit behavior. Do not
change the board size, window dimensions, caption, or other existing launcher
behavior. Do not modify `map_demo.py` or `BoardView`.

## Validation

Test movement within the board and attempted moves beyond each edge. Check
Python syntax and run a launcher smoke check if the available environment
supports Pygame display initialization.

## Scope

Only the marker helpers and the minimum event/render wiring in
`src/board_launch.py` are in scope. Existing unrelated working-tree changes
must remain untouched.
