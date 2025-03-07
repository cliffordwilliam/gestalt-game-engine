import sys
from pathlib import Path

import pygame
import pygame.freetype
from beartype import beartype

from core.error import error
from core.game import Game


@beartype
# PRIVATE
def get_main_py_abs_path() -> str:
    """Return the absolute path of where this function is called. OS agnostic."""
    if getattr(sys, "frozen", False):
        return str(Path(sys.executable).parent)
    return str(Path(__file__).resolve().parent)


@beartype
def main() -> None:
    # Init needed pygame modules only, not all, If this fail, user can't run pygame
    pygame.display.init()
    pygame.freetype.init()

    # Try to instance game or error loop
    try:
        # Game loop
        Game(get_main_py_abs_path()).run()
    except Exception as e:
        # Error loop
        error(e, get_main_py_abs_path())

    # De init all pygame modules
    pygame.quit()


if __name__ == "__main__":
    main()
