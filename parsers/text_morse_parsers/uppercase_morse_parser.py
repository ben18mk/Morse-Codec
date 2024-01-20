from parsers.text_morse_parsers.abstract.morse_parser_base import MorseParserBase
from parsers.text_morse_parsers.conversion_dictionaries.text_morse_dictionaries import morse_to_char

class UppercaseMorseParser(MorseParserBase):
    def __init__(self):
        super().__init__(lambda item: morse_to_char[item].upper())