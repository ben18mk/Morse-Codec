from abc import ABC
from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE

class MorseParserBase(ABC):
    def __init__(self, morse_item_handler: function):
        self._morse_item_handler = morse_item_handler


    def parse_morse_to_text(self, morse: str) -> str:
        morse_words = morse.split(MORSE_SPACE)
        parsed_words = list(map(
            lambda word: ''.join(
                list(map(
                    self._morse_item_handler,
                    word.split(MORSE_SEPARATOR)
                ))
            ),
            morse_words
        ))
        result = ' '.join(parsed_words)
        return result