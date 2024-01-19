from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from encoders.abstract.morse_encoder_base import MorseEncoderBase
from parsers.text_morse_parsers.conversion_dictionaries.text_morse_dictionaries import char_to_morse
from parsers.conversion_dictionaries.morse_bin_parser import parse_morse_to_bin
from utils.string_mapping_utils import map_chars_through_words

class MorseEncoder(MorseEncoderBase):
    def encode(self, text: str) -> bytes:
        morse = map_chars_through_words(
            text,
            ' ',
            None,
            MORSE_SPACE,
            MORSE_SEPARATOR,
            lambda char: char_to_morse[char.upper()]
        )
        morse_bin = '0b' + parse_morse_to_bin(morse)
        result = bytes.fromhex(hex(int(morse_bin, 2))[2:])
        return result