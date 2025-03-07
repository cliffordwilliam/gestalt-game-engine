from __future__ import annotations

from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str
    type: str
    value: str


class Object(BaseModel):
    height: float
    id: int
    name: str
    rotation: float
    type: str
    visible: bool
    width: float
    x: float
    y: float
    point: bool | None = None
    properties: list[Property] | None = None


class Layer(BaseModel):
    id: int
    name: str
    opacity: float = Field(..., ge=0.0, le=1.0)
    type: str
    visible: bool
    x: float
    y: float
    data: list[int] | None = None
    height: float | None = None
    width: float | None = None
    draworder: str | None = None
    objects: list[Object] | None = None
    color: str | None = None


class Tileset(BaseModel):
    firstgid: int
    source: str


class TiledMapDto(BaseModel):
    compressionlevel: int
    height: int
    infinite: bool
    layers: list[Layer]
    nextlayerid: int
    nextobjectid: int
    orientation: str
    renderorder: str
    tiledversion: str
    tileheight: int
    tilesets: list[Tileset]
    tilewidth: int
    type: str
    version: str
    width: int
