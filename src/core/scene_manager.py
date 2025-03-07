from core.event import Event
from core.settings import Settings
from nodes.base_node import BaseNode, BaseNodeParams
from nodes.scenes.gameplay.gameplay import Gameplay


class SceneManager:
    def __init__(self, settings: Settings, event: Event) -> None:
        self.settings = settings
        self.event = event
        self.is_exit = False

        # List of all scenes in the game
        self.scenes: dict[str, type[BaseNode]] = {
            "Gameplay": Gameplay,
        }
        self.current_scene = self.scenes[self.settings.main_scene_name](
            BaseNodeParams(self.settings, self.event, self)
        )

    def run(self, dt: int) -> bool:
        # Draw current scene
        self.current_scene.draw(self.settings.window_surf)

        # Todo: do not update current scene if game is paused
        self.current_scene.update(dt)

        # Tell owner if a scene wanted to end the game loop
        return self.is_exit
