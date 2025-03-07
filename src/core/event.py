from typing import cast

import pygame
from beartype import beartype

from core.settings import Settings


@beartype
class Event:
    def __init__(self, settings: Settings) -> None:
        # PRIVATE
        self.settings = settings
        # PRIVATE
        self.any_key_just_pressed = 0
        # PRIVATE
        self.just_pressed = pygame.key.get_just_pressed()
        # PRIVATE
        self.just_released = pygame.key.get_just_released()
        # PRIVATE
        self.pressed = pygame.key.get_pressed()
        # PRIVATE
        self.just_pressed_mouse = pygame.mouse.get_just_pressed()
        # PRIVATE
        self.just_released_mouse = pygame.mouse.get_just_released()
        # PRIVATE
        self.pressed_mouse = pygame.mouse.get_pressed()

    # PUB
    def update(self) -> bool:
        """
        Update input props.
        Return true if window X pressed.
        """
        # Reset any key just pressed
        self.any_key_just_pressed = 0

        for event in pygame.event.get([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP]):
            # Handle window X exit button
            if event.type == pygame.QUIT:
                return True
            # Update any key just pressed
            elif event.type == pygame.KEYDOWN:
                self.any_key_just_pressed = cast(int, event.key)

        # Update other inputs
        self.just_pressed = pygame.key.get_just_pressed()
        self.just_released = pygame.key.get_just_released()
        self.pressed = pygame.key.get_pressed()
        self.just_pressed_mouse = pygame.mouse.get_just_pressed()
        self.just_released_mouse = pygame.mouse.get_just_released()
        self.pressed_mouse = pygame.mouse.get_pressed()

        return False

    # PUB
    def is_action_just_pressed(self, action: str) -> bool:
        return bool(self.just_pressed[cast(int, getattr(self.settings, action))])

    # PUB
    def is_action_just_released(self, action: str) -> bool:
        return bool(self.just_released[cast(int, getattr(self.settings, action))])

    # PUB
    def is_action_pressed(self, action: str) -> bool:
        return bool(self.pressed[cast(int, getattr(self.settings, action))])

    # PUB
    def is_action_just_pressed_mouse(self, action: str) -> bool:
        return bool(self.just_pressed_mouse[cast(int, getattr(self.settings, action))])

    # PUB
    def is_action_just_released_mouse(self, action: str) -> bool:
        return bool(self.just_released_mouse[cast(int, getattr(self.settings, action))])

    # PUB
    def is_action_pressed_mouse(self, action: str) -> bool:
        return bool(self.pressed_mouse[cast(int, getattr(self.settings, action))])

    # PUB
    def get_direction_horizontal(self) -> int:
        return self.is_action_just_pressed(
            self.settings.right_key_name
        ) - self.is_action_just_pressed(self.settings.left_key_name)
