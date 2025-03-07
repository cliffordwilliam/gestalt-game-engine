import pygame
from beartype import beartype

from nodes.base_node import BaseNode, BaseNodeParams


@beartype
class Test(BaseNode):
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

    # PUB
    def draw(self, window_surf: pygame.Surface) -> None:
        window_surf.fill(self.settings.color_white)

    # PUB
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
