from typing import cast

import pygame

from core.settings import Settings


class Event:
    def __init__(self, settings: Settings) -> None:
        # To read input map, what is the up input? W or up arrow?
        self.settings = settings

        # Query these once every frame before doing anything else
        self.just_pressed = pygame.key.get_just_pressed()
        self.just_released = pygame.key.get_just_released()
        self.pressed = pygame.key.get_pressed()
        self.just_pressed_mouse = pygame.mouse.get_just_pressed()
        self.just_released_mouse = pygame.mouse.get_just_released()
        self.pressed_mouse = pygame.mouse.get_pressed()

        # Hold scancode of just pressed key this frame
        self.anything_just_pressed = 0

    def update(self) -> bool:
        # Reset anything just pressed scancode
        self.anything_just_pressed = 0

        # Pump events
        for event in pygame.event.get([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP]):
            # Handle telling main loop to break
            if event.type == pygame.QUIT:
                return True
            # Handle anything just pressed
            elif event.type == pygame.KEYDOWN:
                self.anything_just_pressed = cast(int, event.key)

        # Query these once every frame before doing anything else
        self.just_pressed = pygame.key.get_just_pressed()
        self.just_released = pygame.key.get_just_released()
        self.pressed = pygame.key.get_pressed()
        self.just_pressed_mouse = pygame.mouse.get_just_pressed()
        self.just_released_mouse = pygame.mouse.get_just_released()
        self.pressed_mouse = pygame.mouse.get_pressed()

        # Tell main window top right X button was not clicked this frame
        return False

    def is_action_just_pressed(self, action: str) -> bool:
        return bool(self.just_pressed[cast(int, getattr(self.settings, action))])

    def is_action_just_released(self, action: str) -> bool:
        return bool(self.just_released[cast(int, getattr(self.settings, action))])

    def is_action_pressed(self, action: str) -> bool:
        return bool(self.pressed[cast(int, getattr(self.settings, action))])

    def get_direction_horizontal(self) -> int:
        return self.is_action_just_pressed(
            self.settings.right_key_name
        ) - self.is_action_just_pressed(self.settings.left_key_name)
