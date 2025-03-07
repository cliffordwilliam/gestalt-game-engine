import pygame

from core.event import Event
from core.scene_manager import SceneManager
from core.settings import Settings


class Loop:
    def __init__(
        self, settings: Settings, event: Event, scene_manager: SceneManager
    ) -> None:
        self.settings = settings
        self.event = event
        self.scene_manager = scene_manager
        self.dt = (
            1  # Because very first frame dt is 0, need to make it 1 so timer works
        )

    def run(self) -> None:
        # The game loop
        while 1:
            # Handle top right window x exit button
            if self.event.update():
                break

            # Wipe window surface
            self.settings.wipe_native_surf()

            # Run current scene and handle if a scene wants to end the game loop
            if self.scene_manager.run(self.dt):
                break

            # Update dt
            self.dt = self.settings.end_frame_cleanup()

            # REMOVE IN PROD
            pygame.display.set_caption(f"FPS: {self.settings.clock.get_fps():.0f}")
