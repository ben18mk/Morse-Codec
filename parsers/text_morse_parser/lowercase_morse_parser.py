from parsers.text_morse_parser.abstract.morse_parser_base import MorseParserBase
from parsers.text_morse_parser.convertor_dictionaries.text_morse_dictionaries import morse_to_char

class LowercaseMorseParser(MorseParserBase):
    def __init__(self):
        super().__init__(lambda item: morse_to_char[item].lower())