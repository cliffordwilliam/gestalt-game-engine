from pathlib import Path

import pygame
import pygame.freetype
from beartype import beartype


@beartype
class Settings:
    def __init__(self, main_py_abs_path: str) -> None:
        # Main.py absolute path
        # PRIVATE
        self.main_py_abs_path = main_py_abs_path

        # File names
        # PRIVATE
        self.traceback_file_name = "traceback.out"
        # PRIVATE
        self.font_file_name = "cg_pixel_3x5_mono.ttf"
        # PRIVATE
        self.first_room_json_file_name = "small_room.json"

        # Dir names
        # PRIVATE
        self.fonts_folder_name = "fonts"
        # PRIVATE
        self.database_folder_name = "database"
        # PRIVATE
        self.assets_folder_name = "assets"
        # PRIVATE
        self.jsons_folder_name = "jsons"
        # PRIVATE
        self.images_folder_name = "images"

        # File paths
        # PRIVATE
        self.traceback_file_path = Path(
            self.main_py_abs_path,
            self.database_folder_name,
            self.traceback_file_name,
        )
        # PRIVATE
        self.font_file_path = Path(
            self.main_py_abs_path,
            self.assets_folder_name,
            self.fonts_folder_name,
            self.font_file_name,
        )

        # Dir paths
        # PRIVATE
        self.json_folder_path = Path(
            self.main_py_abs_path,
            self.assets_folder_name,
            self.jsons_folder_name,
        )
        # PRIVATE
        self.images_folder_path = Path(
            self.main_py_abs_path,
            self.assets_folder_name,
            self.images_folder_name,
        )

        # Font prop
        # PRIVATE
        self.font_width = 3
        # PRIVATE
        self.font_height = 5
        # PRIVATE
        self.letter_width = 4
        # PRIVATE
        self.letter_height = 6
        # PRIVATE
        self.letter_gap_y = 5
        # PRIVATE
        self.font = pygame.freetype.Font(self.font_file_path, self.font_height)

        # Pygame settings
        # PRIVATE
        self.native_width = 320
        # PRIVATE
        self.native_height = 180
        # PRIVATE
        self.clock = pygame.time.Clock()
        # PRIVATE
        self.fps = 60
        # PRIVATE
        self.tile_size = 16

        # Window surf and rect
        # PRIVATE
        self.window_surf = pygame.display.set_mode(
            (self.native_width, self.native_height), pygame.SCALED
        )
        # PRIVATE
        self.window_rect = self.window_surf.get_rect()

        # Keyboard names
        # PRIVATE
        self.up_key_name = "up_key"
        # PRIVATE
        self.down_key_name = "down_key"
        # PRIVATE
        self.left_key_name = "left_key"
        # PRIVATE
        self.right_key_name = "right_key"
        # PRIVATE
        self.confirm_key_name = "confirm_key"
        # PRIVATE
        self.pause_key_name = "pause_key"
        # PRIVATE
        self.jump_key_name = "jump_key"
        # PRIVATE
        self.attack_key_name = "attack_key"

        # Input map
        # PUB
        # TODO: Make a save and load to update this later
        # TODO: Make setters later to update game
        self.up_key = 1073741906
        # PUB
        self.down_key = 1073741905
        # PUB
        self.left_key = 1073741904
        # PUB
        self.right_key = 1073741903
        # PUB
        self.confirm_key = 13
        # PUB
        self.pause_key = 27
        # PUB
        self.jump_key = 99
        # PUB
        self.attack_key = 120

        # Colors
        # PRIVATE
        self.color_white = "white"
        # PRIVATE
        self.color_blue = "#000080"

        # Game settings prop
        # PUB
        # TODO: Make a save and load to update this later
        # TODO: Make setters later to update game
        self.is_fullscreen = 1
        # PUB
        self.difficulty = 1
        # PUB
        self.minimap = 1
        # PUB
        self.brightness = 50
        # PUB
        self.music_volume = 50
        # PUB
        self.sfx_volume = 50
        # PUB
        self.speech_volume = 50
        # PUB
        self.screen_shake = 1
        # PUB
        self.camera_responsiveness = 50

        # Room spritesheet width is fixed for this game
        self.spritesheet_width = 32

    # PUB CORE
    def wipe_native_surf(self) -> None:
        self.window_surf.fill(self.color_blue)

    # PUB CORE
    def end_frame_cleanup(self) -> int:
        pygame.display.update()
        return self.clock.tick(self.fps)
