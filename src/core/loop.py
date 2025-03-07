import pygame
from beartype import beartype

from core.event import Event
from core.scene_manager import SceneManager
from core.settings import Settings


@beartype
class Loop:
    def __init__(
        self, settings: Settings, event: Event, scene_manager: SceneManager
    ) -> None:
        # PRIVATE
        self.settings = settings
        # PRIVATE
        self.event = event
        # PRIVATE
        self.scene_manager = scene_manager

        # PRIVATE
        self.dt = 1  # Very first game frame dt is 0, it needs to be 1 so timer works

    # PUB CORE
    def run(self) -> None:
        """
        Handle window X exit button
        Wipe window surface
        Run scene manager
        Update dt
        """
        while 1:
            # Handle window X exit button
            if self.event.update():
                break

            # Wipe window surface
            self.settings.wipe_native_surf()

            # Run current scene and handle in game exit button
            if self.scene_manager.run(self.dt):
                break

            # Update dt
            self.dt = self.settings.end_frame_cleanup()

            # REMOVE IN PROD
            pygame.display.set_caption(f"FPS: {self.settings.clock.get_fps():.0f}")
