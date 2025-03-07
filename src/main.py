import sys
from os import path

import pygame
import pygame.freetype
from beartype import beartype

from core.game import Game


@beartype
# PRIVATE
def _get_main_py_abs_path() -> str:
    """
    Returns absolute str path of where this func is called. OS agnostic.
    """
    if getattr(sys, "frozen", False):
        return path.dirname(sys.executable)
    return path.dirname(path.abspath(__file__))


@beartype
def main() -> None:
    # Init needed pygame modules only, not all, If this fail, user can't run pygame
    pygame.display.init()
    pygame.freetype.init()

    # Run game loop or error loop
    Game(_get_main_py_abs_path()).run()

    # De init all pygame modules
    pygame.quit()


if __name__ == "__main__":
    main()
