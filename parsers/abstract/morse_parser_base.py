from abc import ABC
from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE

class MorseParserBase(ABC):
    def parse_morse_to_text(morse: str, morse_item_handler: function) -> str:
        morse_words = morse.split(MORSE_SPACE)
        parsed_words = list(map(
            lambda word: ''.join(
                list(map(
                    morse_item_handler,
                    word.split(MORSE_SEPARATOR)
                ))
            ),
            morse_words
        ))
        result = ' '.join(parsed_words)
        return result