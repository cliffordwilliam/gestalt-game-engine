import sys
from os import path

from core.game import Game


def _get_main_py_abs_path() -> str:
    if getattr(sys, "frozen", False):
        return path.dirname(sys.executable)
    return path.dirname(path.abspath(__file__))


def main() -> None:
    main_py_abs_path: str = _get_main_py_abs_path()
    # Try to instance game
    game = Game.core_initialize(main_py_abs_path)
    if game:
        game.run()
    # If instance game and error game loop fail, then user machine cannot run pygame


if __name__ == "__main__":
    main()
