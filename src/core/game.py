import pygame
import pygame.freetype

from core.error import error
from core.event import Event
from core.loop import Loop
from core.scene_manager import SceneManager
from core.settings import Settings


class Game:
    def __init__(self, main_py_abs_path: str) -> None:
        self.main_py_abs_path = main_py_abs_path

        # Init needed pygame modules only, not all
        pygame.display.init()
        pygame.freetype.init()

        # Reference to other cores
        self.settings = Settings(self.main_py_abs_path)
        self.event = Event(self.settings)
        self.scene_manager = SceneManager(self.settings, self.event)
        self.loop = Loop(self.settings, self.event, self.scene_manager)

    def run(self) -> None:
        # Runs the main game loop
        try:
            self.loop.run()
        # Catch error from main game loop
        except Exception as e:
            error(e, self.main_py_abs_path)
        # De init all pygame modules on exit
        finally:
            pygame.quit()

    @classmethod
    def core_initialize(cls, main_py_abs_path: str) -> "Game | None":
        # Try to instance game
        try:
            return Game(main_py_abs_path)
        # If cannot instance game then show error game loop
        except Exception as e:
            error(e, main_py_abs_path)
            pygame.quit()
            return None
