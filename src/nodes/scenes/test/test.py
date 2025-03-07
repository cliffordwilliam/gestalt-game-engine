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
    def draw(self, _window_surf: pygame.Surface) -> None:
        _window_surf.fill(self.settings.color_white)

    # PUB
    def update(self, dt: int) -> None:
        if self.event.is_action_just_pressed(self.settings.attack_key_name):
            self.scene_manager.set_current_scene(self.scene_manager.gameplay_scene_name)

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
