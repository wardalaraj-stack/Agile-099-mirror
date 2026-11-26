# Setup

Make sure you have Python 3.14 on your machine.
https://www.python.org/downloads/

This project uses pygame-ce 2.5.8, which supports Python 3.14.
Make sure to install pygame-ce rather than regular pygame.

If you're unsure, VS Code will ask for version during setup.

## Visual Studio Code (VSC)

Open VSC and go to Extensions.
Search for Python and install the extension by Microsoft.

Open the agile-099 folder and select Python 3.14 as your Python interpreter.

## Dependencies

Open the terminal and run:

`python -m pip install -r config/requirements.txt`

Alternatively, install the required package directly:

`python -m pip install pygame-ce==2.5.8`

Make sure the installation uses Python 3.14.

## Environment (optional)

Open the command palette and search for
`Python: Create Environment`.

Select `venv` and then select Python 3.13 from the list of available versions.

When asked to name the environment, enter `.venv`

Select `Install project dependencies` and then select `config/requirements.txt`.
Wait for the installation to finish.

## Game

Open `main.py` and press the run button.

You only need to go through the setup once.
The next time you open the project, simply run `main.py`.
