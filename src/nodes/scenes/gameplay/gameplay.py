import json
import os
from os import path

import pygame
from beartype import beartype
from dacite import from_dict

from nodes.base_node import BaseNode, BaseNodeParams
from nodes.scenes.gameplay.definitions.tiled_map_dto import TiledMapDto


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
        # PRIVATE
        self.first_room_name = "test_room.json"
        # PRIVATE
        self.tile_sheet_name = ""
        # PRIVATE
        self.spritesheet = pygame.Surface((0, 0))
        # PRIVATE
        self.room_width = 0.0
        # PRIVATE
        self.room_height = 0.0
        # PRIVATE
        self.pre_rendered_bg: pygame.Surface = pygame.Surface(
            (
                self.room_width * self.settings.tile_size,
                self.room_height * self.settings.tile_size,
            ),
            pygame.SRCALPHA,
        )

        ############
        # Instance #
        ############
        # None

        ############
        # On ready #
        ############
        self.read_tilemap_json(self.first_room_name)

    ####################
    # Signal callbacks #
    ####################
    # None

    ###################
    # Frame callbacks #
    ###################

    # PUB CORE
    def draw(self, window_surf: pygame.Surface) -> None:
        # Draw pre rendered bg
        window_surf.blit(self.pre_rendered_bg)

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
    def read_tilemap_json(self, room_name: str) -> None:
        """
        Reads room json to
        Render bg
        Make collision lookup string
        """
        # Read json, throws if invalid dto shape
        with open(path.join(self.settings.json_folder_path, room_name), "r") as file:
            data = from_dict(data_class=TiledMapDto, data=json.load(file))

        # Update room size and get new pre rendered bg paper
        self.room_width = data.width
        self.room_height = data.height
        self.pre_rendered_bg = pygame.Surface(
            (
                self.room_width * self.settings.tile_size,
                self.room_height * self.settings.tile_size,
            ),
            pygame.SRCALPHA,
        )

        # Get tile sheet name
        self.tile_sheet_name = os.path.splitext(data.tilesets[0].source)[0]

        # Get tile sheet image
        self.spritesheet = pygame.image.load(
            path.join(self.settings.images_folder_path, f"{self.tile_sheet_name}.png")
        ).convert_alpha()

        # Iter json
        for index, layer in enumerate(data.layers):
            if not layer.data:
                continue
            # Draw pre rendered bg
            for index, tile_id in enumerate(layer.data):
                tile_id -= 1
                if tile_id == -1:
                    continue
                # Calc destination on world
                x = index % self.room_width
                y = index // self.room_width
                dest_x = x * self.settings.tile_size
                dest_y = y * self.settings.tile_size
                # Get spritesheet region position
                src_x = (
                    tile_id % self.settings.spritesheet_width
                ) * self.settings.tile_size
                src_y = (
                    tile_id // self.settings.spritesheet_width
                ) * self.settings.tile_size
                # Start painting the pre rendered bg
                self.pre_rendered_bg.blit(
                    self.spritesheet,
                    (dest_x, dest_y),
                    (src_x, src_y, self.settings.tile_size, self.settings.tile_size),
                )

    ##########
    # Setget #
    ##########
    # None
