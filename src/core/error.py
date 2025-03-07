import logging
import traceback
from os import makedirs, path
from os.path import dirname

import pygame
import pygame.freetype
from beartype import beartype

from utils.write import write


@beartype
def error(exception: Exception, main_py_abs_path: str) -> None:
    # Draw err text on window surf
    native_width = 320
    native_height = 180
    color_blue = "#000080"
    database_folder_name = "database"
    traceback_file_name = "traceback.out"
    traceback_file_path = path.join(
        main_py_abs_path,
        database_folder_name,
        traceback_file_name,
    )
    assets_folder_name = "assets"
    fonts_folder_name = "fonts"
    font_file_name = "cg_pixel_3x5_mono.ttf"
    font_height = 5
    letter_height = 6
    letter_gap_y = 5
    letter_width = 4
    font_file_path = path.join(
        main_py_abs_path,
        assets_folder_name,
        fonts_folder_name,
        font_file_name,
    )
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.freetype.Font(font_file_path, font_height)
    window_surf = pygame.display.set_mode((native_width, native_height), pygame.SCALED)
    window_surf.fill(color_blue)
    error_text = f"{exception} {traceback.format_exc()}"
    write(
        window_surf,
        (
            f"An exception has occurred:\n\n"
            f"See {traceback_file_path} for details\n\n"
            f"{error_text}"
        ),
        font,
        "white",
        letter_gap_y,
        letter_width,
        letter_height,
    )

    # Get traceback dir
    directory = dirname(traceback_file_path)
    makedirs(directory, exist_ok=True)

    # Init logger
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(traceback_file_path)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False

    # Write to disk
    logger.error(error_text)
    print(error_text)

    # Starts the loop
    running = 1

    # Error game loop
    while running:
        # Handle window X exit button
        for _event in pygame.event.get(pygame.QUIT):
            running = 0
        # If not dragging the window will mess up renders
        pygame.display.update()
        # Limit fps
        clock.tick(fps)
