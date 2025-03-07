import logging
import traceback
from os import makedirs, path
from os.path import dirname

import pygame
import pygame.freetype


def error(exception: Exception, main_py_abs_path: str) -> None:
    # Init loop
    pygame.display.init()
    pygame.freetype.init()
    screen = pygame.display.set_mode((320, 180), pygame.SCALED)
    clock = pygame.time.Clock()

    # Draw
    screen.fill("#000080")
    font = pygame.freetype.Font(file=None, size=5)
    font.origin = True
    error_text = f"{exception} {traceback.format_exc()}"

    # Get traceback path
    traceback_file_path = path.join(main_py_abs_path, "traceback.out")

    # Make dir
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
    logger.error(traceback.format_exc())

    # REMOVE IN PROD
    print(error_text)

    # Starts the loop
    running = True

    # Error game loop
    while running:
        # Handle top right window x exit button
        for _event in pygame.event.get(pygame.QUIT):
            running = False
        # If not dragging the window will mess up renders
        pygame.display.update()
        # Limit fps
        clock.tick(60)
