"""Check the grid, edge movements, and drawing commands without a window."""

import unittest

from src.map_demo import CELL_SIZE, MARGIN, draw_map, next_position
from src.map_grid import MapGrid


class RecordingCanvas:
    """Store the rectangles that draw_map asks the canvas to draw."""

    def __init__(self):
        """Start with an empty list of rectangle calls."""
        self.rectangles = []

    def create_rectangle(self, left, top, right, bottom, **options):
        """Save rectangle corners and the tag used to identify the shape."""
        corners = (left, top, right, bottom)
        tag = options.get("tags")
        self.rectangles.append((corners, tag))


class MapGridTests(unittest.TestCase):
    """Use a rectangular grid so swapped rows and columns are noticeable."""

    def setUp(self):
        """Give every test a fresh grid with four columns and three rows."""
        self.grid = MapGrid(width=4, height=3)

    def test_rectangular_grid_has_exactly_the_expected_cells(self):
        """Check the order and uniqueness of all twelve positions."""
        expected_cells = [
            (0, 0), (1, 0), (2, 0), (3, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),
        ]

        actual_cells = list(self.grid.cells())

        self.assertEqual(actual_cells, expected_cells)
        self.assertEqual(len(set(actual_cells)), 12)

    def test_corner_cells_are_inside(self):
        """Check that the first and last row and column are still inside."""
        corners = [(0, 0), (3, 0), (0, 2), (3, 2)]

        for position in corners:
            with self.subTest(position=position):
                self.assertTrue(self.grid.contains(position))
                self.assertEqual(self.grid.outside_edges(position), ())

    def test_one_cell_past_each_boundary(self):
        """Check the first outside position on all four sides."""
        edge_cases = [
            ((-1, 1), ("left",)),
            ((4, 1), ("right",)),
            ((1, -1), ("top",)),
            ((1, 3), ("bottom",)),
        ]

        for position, expected_edges in edge_cases:
            with self.subTest(position=position):
                actual_edges = self.grid.outside_edges(position)

                self.assertFalse(self.grid.contains(position))
                self.assertEqual(actual_edges, expected_edges)

    def test_diagonal_exit_reports_both_sides(self):
        """Check that a position past a corner reports both crossed edges."""
        above_left = self.grid.outside_edges((-1, -1))
        below_right = self.grid.outside_edges((4, 3))

        self.assertEqual(above_left, ("left", "top"))
        self.assertEqual(below_right, ("right", "bottom"))

    def test_one_cell_grid(self):
        """Check that a one-cell grid only contains its origin."""
        small_grid = MapGrid(1, 1)

        self.assertEqual(list(small_grid.cells()), [(0, 0)])
        self.assertTrue(small_grid.contains((0, 0)))
        self.assertFalse(small_grid.contains((1, 0)))

    def test_invalid_dimensions_and_fractional_cell(self):
        """Check that invalid sizes and fractional coordinates fail clearly."""
        # Invalid values and invalid types raise different kinds of errors.
        with self.assertRaises(ValueError):
            MapGrid(0, 3)
        with self.assertRaises(ValueError):
            MapGrid(4, -1)
        with self.assertRaises(TypeError):
            MapGrid(2.5, 3)
        with self.assertRaises(TypeError):
            self.grid.contains((0.5, 1))

    def test_demo_draws_all_tiles_and_exactly_one_outer_frame(self):
        """Check the drawing commands for twelve tiles and one outer frame."""
        canvas = RecordingCanvas()

        draw_map(canvas, self.grid)

        rectangles = canvas.rectangles
        self.assertEqual(len(rectangles), 13)
        # The first twelve commands must all be tiles. The last is the frame.
        for _, tag in rectangles[:12]:
            self.assertEqual(tag, "cell")

        first_cell = (MARGIN, MARGIN, MARGIN + CELL_SIZE, MARGIN + CELL_SIZE)
        self.assertEqual(rectangles[0], (first_cell, "cell"))

        expected_frame = (
            MARGIN,
            MARGIN,
            MARGIN + 4 * CELL_SIZE,
            MARGIN + 3 * CELL_SIZE,
        )
        self.assertEqual(rectangles[-1], (expected_frame, "outer_frame"))

    def test_demo_marker_stays_inside_after_attempted_exit(self):
        """Check a valid right step and a right step that hits the edge."""
        step_right = (1, 0)

        valid_move = next_position(self.grid, (2, 2), step_right)
        outside_move = next_position(self.grid, (3, 2), step_right)

        self.assertEqual(valid_move, ((3, 2), ()))
        self.assertEqual(outside_move, ((3, 2), ("right",)))


if __name__ == "__main__":
    unittest.main()
