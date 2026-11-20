# 11.1 Create a snake head

Implementation of the snake head for GitLab issue #32.

## Requirements

Python 3.13 and Pygame 2.6.1.

## Setup

### Mac/Linux

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python demo_snake.py
```

## Design

### Snake (snake.py)

The Snake class is responsible for snake's game state.

The attributes are private. Getter methods provide access to state.

Head position is stored as a tuple, representing its position on the board.

The body is currently an empty list, prepared for future implementation.
get_body() returns a copy to prevent other classes from modifying the original list directly.

### SnakeRenderer (snake_renderer.py)

Responsible for drawing the snake using Pygame.

Retrieves position and color through the Snake class methods.
Converts the coordinates into pixel coordinates, and draws the head.

Cell size is provided when creating the renderer.
Should be able to adapt to different board dimensions dynamically without modifying the Snake class.
