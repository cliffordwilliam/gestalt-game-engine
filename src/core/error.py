import logging
import traceback
from os import makedirs
from os.path import dirname

import pygame
import pygame.freetype
from beartype import beartype

from core.settings import Settings
from utils.write import write


@beartype
def error(exception: Exception, settings: Settings) -> None:
    # Draw err text on window surf
    settings.window_surf.fill(settings.color_blue)
    error_text = f"{exception} {traceback.format_exc()}"
    write(
        settings.window_surf,
        (
            f"An exception has occurred:\n\n"
            f"See {settings.traceback_file_path} for details\n\n"
            f"{error_text}"
        ),
        settings.font,
        "white",
        settings.letter_gap_y,
        settings.letter_width,
        settings.letter_height,
    )

    # Get traceback dir
    directory = dirname(settings.traceback_file_path)
    makedirs(directory, exist_ok=True)

    # Init logger
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(settings.traceback_file_path)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False

    # Write to disk
    logger.error(error_text)

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
        settings.clock.tick(settings.fps)
