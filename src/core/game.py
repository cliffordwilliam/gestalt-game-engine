from beartype import beartype

from core.error import error
from core.event import Event
from core.loop import Loop
from core.scene_manager import SceneManager
from core.settings import Settings


@beartype
class Game:
    """
    Holds other game cores.
    """

    def __init__(self, main_py_abs_path: str) -> None:
        # PRIVATE
        self.main_py_abs_path = main_py_abs_path

        # PRIVATE
        self.settings = Settings(self.main_py_abs_path)
        # PRIVATE
        self.event = Event(self.settings)
        # PRIVATE
        self.scene_manager = SceneManager(self.settings, self.event)
        # PRIVATE
        self.loop = Loop(self.settings, self.event, self.scene_manager)

    # PUB CORE
    def run(self) -> None:
        """
        Run game loop or error loop.
        """
        try:
            # Game loop
            self.loop.run()
        except Exception as e:
            # Error loop
            error(e, self.main_py_abs_path)
