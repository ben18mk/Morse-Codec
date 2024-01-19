from abc import ABC, abstractclassmethod
from parsers.abstract.morse_parser_base import MorseParserBase

class MorseDecoderBase(ABC):
    def __init__(self, morse_parser: MorseParserBase):
        self._morse_parser = morse_parser


    @abstractclassmethod
    def decode(self, data: bytes) -> str:
        pass