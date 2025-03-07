import pygame
import pygame.freetype
from beartype import beartype


@beartype
def write(
    surf: pygame.Surface,
    text: str,
    _font: pygame.freetype.Font,
    color: str,
    gap_y: int,
    _letter_width: int,
    _letter_height: int,
) -> None:
    # If paper is smaller than 1 letter just return early
    is_paper_smaller_than_one_letter = (
        surf.width < _letter_width or surf.height < _letter_height
    )
    if is_paper_smaller_than_one_letter:
        return

    # Cursor position
    cursor_x = 0
    cursor_y = 0

    # Letters to write
    letters = list(text)

    # Draw
    for letter in letters:
        # Letter right side or outside paper?
        if cursor_x + _letter_width > surf.width:
            # Move cursor to new line and most left
            cursor_x = 0
            cursor_y += _letter_height + gap_y

        # Cursor bottom overshoot paper bottom?
        if cursor_y + _letter_height > surf.height:
            # Stop writing
            return

        # \n char found?
        if letter == "\n":
            # Move cursor to new line and most left
            cursor_x = 0
            cursor_y += _letter_height + gap_y
            # Do not draw this
            continue

        # Draw letter on paper
        _font.render_to(surf, (cursor_x, cursor_y), letter, color)

        # Move cursor to right
        cursor_x += _letter_width
