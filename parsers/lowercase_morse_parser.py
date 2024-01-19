from parsers.abstract.morse_parser_base import MorseParserBase
from parsers.conversion_dictionaries.morse_parser_dictionaries import morse_to_char

class LowercaseMorseParser(MorseParserBase):
    def parse_morse_to_text(morse: str, morse_item_handler: function) -> str:
        return super().parse_morse_to_text(
            morse,
            lambda item: morse_to_char[item].lower()
        )