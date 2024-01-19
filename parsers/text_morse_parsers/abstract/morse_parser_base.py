from abc import ABC
from collections.abc import Callable
from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from utils.string_mapping_utils import map_chars_through_words

class MorseParserBase(ABC):
    def __init__(self, morse_item_handler: Callable):
        self._morse_item_handler = morse_item_handler


    def parse_morse_to_text(self, morse: str) -> str:
        result = map_chars_through_words(
            morse,
            MORSE_SPACE,
            MORSE_SEPARATOR,
            ' ',
            '',
            self._morse_item_handler
        )
        return result