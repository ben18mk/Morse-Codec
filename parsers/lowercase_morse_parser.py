from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from parsers.abstract.morse_parser_base import MorseParserBase
from parsers.conversion_dictionaries.morse_parser_dictionaries import morse_to_char

class LowercaseMorseParser(MorseParserBase):
    def parse_morse_to_text(morse: str) -> str:
        morse_words = morse.split(MORSE_SPACE)
        parsed_words = list(map(
            lambda word: ''.join(
                list(map(
                    lambda item: morse_to_char[item].lower(),
                    word.split(MORSE_SEPARATOR)
                ))
            ),
            morse_words
        ))
        result = ' '.join(parsed_words)
        return result