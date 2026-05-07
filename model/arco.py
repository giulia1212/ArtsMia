from dataclasses import dataclass

from model.artObject import ArtObject

@ dataclass
class Arco:
    o1: ArtObject
    o2: ArtObject
    peso: int