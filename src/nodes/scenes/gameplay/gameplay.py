import pygame
from beartype import beartype

from nodes.base_node import BaseNode, BaseNodeParams


@beartype
class Gameplay(BaseNode):
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
        super().__init__(base_node_params)

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
    def draw(self, _window_surf: pygame.Surface) -> None:
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
