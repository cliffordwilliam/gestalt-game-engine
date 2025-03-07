from beartype import beartype

from core.event import Event
from core.settings import Settings
from nodes.base_node import BaseNode, BaseNodeParams
from nodes.scenes.gameplay.gameplay import Gameplay
from nodes.scenes.test.test import Test


@beartype
class SceneManager:
    def __init__(self, settings: Settings, event: Event) -> None:
        # PRIVATE
        self.settings: Settings = settings
        # PRIVATE
        self.event: Event = event

        # Dictionary mapping SceneName enum values to scene classes
        # PRIVATE
        self.gameplay_scene_name = "Gameplay"
        # PRIVATE
        self.test_scene_name = "Test"
        # PRIVATE
        self.scenes: dict[str, type[BaseNode]] = {
            self.gameplay_scene_name: Gameplay,
            self.test_scene_name: Test,
        }

        # PUB
        # Change this to swtich scene with setter
        self.current_scene: BaseNode = self.scenes[self.gameplay_scene_name](
            BaseNodeParams(self.settings, self.event, self)
        )

        # PUB
        # Change this to end loop with setter
        self.is_exit = False

    # PUB
    # Change this to swtich scene with setter
    # TODO: Do data binding per image / json to each scenes
    def set_current_scene(self, scene: str) -> None:
        self.current_scene = self.scenes[scene](
            BaseNodeParams(self.settings, self.event, self)
        )

    # PUB
    # Change this to end loop with setter
    def set_is_exit_true(self) -> None:
        self.is_exit = True

    # PUB CORE
    def run(self, dt: int) -> bool:
        """
        Draw current scene.
        Update current scene.
        Return true if scene wants to quit.
        """
        # Draw current scene
        self.current_scene.draw(self.settings.window_surf)

        # Update current scene
        self.current_scene.update(dt)

        # Tell owner if a scene wanted to end the game loop
        return self.is_exit
