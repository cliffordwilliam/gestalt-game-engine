import pygame
import pygame.freetype


class Settings:
    def __init__(self, main_py_abs_path: str) -> None:
        self.main_py_abs_path = main_py_abs_path

        # First scene to start
        self.main_scene_name = "Gameplay"

        # Pygame settings
        self.native_width = 320
        self.native_height = 180
        self.clear_surf_color = "#000080"
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.tile_size = 16

        # Window surf and rect
        self.window_surf = pygame.display.set_mode(
            (self.native_width, self.native_height), pygame.SCALED
        )
        self.window_rect = self.window_surf.get_rect()

        # Game settings prop
        self.is_fullscreen = 1
        self.difficulty = 1
        self.minimap = 1
        self.brightness = 50
        self.music_volume = 50
        self.sfx_volume = 50
        self.speech_volume = 50
        self.screen_shake = 1
        self.camera_responsiveness = 50

        # Input map
        self.up_key = 1073741906
        self.down_key = 1073741905
        self.left_key = 1073741904
        self.right_key = 1073741903
        self.confirm_key = 13
        self.pause_key = 27
        self.jump_key = 99
        self.attack_key = 120
        self.up_key_name = "up_key"
        self.down_key_name = "down_key"
        self.left_key_name = "left_key"
        self.right_key_name = "right_key"
        self.confirm_key_name = "confirm_key"
        self.pause_key_name = "pause_key"
        self.jump_key_name = "jump_key"
        self.attack_key_name = "attack_key"

    # Publics
    def wipe_native_surf(self) -> None:
        self.window_surf.fill(self.clear_surf_color)

    def end_frame_cleanup(self) -> int:
        pygame.display.update()
        return self.clock.tick(self.fps)
