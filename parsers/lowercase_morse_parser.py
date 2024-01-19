from parsers.abstract.morse_parser_base import MorseParserBase
from parsers.conversion_dictionaries.morse_parser_dictionaries import morse_to_char

class LowercaseMorseParser(MorseParserBase):
    def __init__(self):
        super().__init__(lambda item: morse_to_char[item].lower())