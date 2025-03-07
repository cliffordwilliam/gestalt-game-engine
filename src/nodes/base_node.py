from dataclasses import dataclass
from typing import TYPE_CHECKING

import pygame
from beartype import beartype

from core.event import Event
from core.settings import Settings

# BaseNode and SceneManager cyclic dependency workaround
if TYPE_CHECKING:
    from core.scene_manager import SceneManager


@dataclass
@beartype
class BaseNodeParams:
    settings: Settings
    event: Event
    scene_manager: "SceneManager"


@beartype
class BaseNode:
    def __init__(
        self,
        ##############
        # Base param #
        ##############
        base_node_params: BaseNodeParams,
        ##################
        # My extra param #
        ##################
        # None
    ) -> None:
        ##############
        # Base param #
        ##############
        self.settings = base_node_params.settings
        self.event = base_node_params.event
        self.scene_manager = base_node_params.scene_manager
        self.base_node_params = base_node_params

        ##################
        # My extra param #
        ##################
        # None

        ###########
        # My prop #
        ###########
        # None

        ############
        # Instance #
        ############
        # None

        ############
        # On ready #
        ############
        # None

    ####################
    # Signal callbacks #
    ####################
    # None

    ###################
    # Frame callbacks #
    ###################

    # PUB CORE
    def draw(self, window_surf: pygame.Surface) -> None:
        pass

    # PUB CORE
    def update(self, dt: int) -> None:
        pass

    ###########
    # Publics #
    ###########
    # None

    ############
    # Privates #
    ############
    # None

    ##########
    # Setget #
    ##########
    # None
