from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Property:
    name: str
    type: str
    value: str


@dataclass
class Object:
    height: float
    id: float
    name: str
    rotation: float
    type: str
    visible: bool
    width: float
    x: float
    y: float
    point: Optional[bool] = None
    properties: Optional[List[Property]] = None


@dataclass
class Layer:
    id: float
    name: str
    opacity: float
    type: str
    visible: bool
    x: float
    y: float
    data: Optional[List[float]] = None
    height: Optional[float] = None
    width: Optional[float] = None
    draworder: Optional[str] = None
    objects: Optional[List[Object]] = None
    color: Optional[str] = None


@dataclass
class Tileset:
    firstgid: float
    source: str


@dataclass
class TiledMapDto:
    compressionlevel: float
    height: float
    infinite: bool
    layers: List[Layer]
    nextlayerid: float
    nextobjectid: float
    orientation: str
    renderorder: str
    tiledversion: str
    tileheight: float
    tilesets: List[Tileset]
    tilewidth: float
    type: str
    version: str
    width: float
