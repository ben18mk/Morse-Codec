from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from encoders.abstract.morse_encoder_base import MorseEncoderBase
from parsers.morse_parser import char_to_morse
from parsers.morse_bin_parser import parse_morse_to_bin

class LowerCaseMorseEncoder(MorseEncoderBase):
    def encode(self, text: str) -> bytes:
        words = text.split(' ')
        morse_list = list(map(
            lambda word: MORSE_SEPARATOR.join(
                list(map(
                    lambda char: char_to_morse[char.upper()],
                    list(word)
                ))
            ),
            words
        ))
        morse = MORSE_SPACE.join(morse_list)
        morse_bin = '0b' + parse_morse_to_bin(morse)
        result = bytes.fromhex(hex(int(morse_bin, 2))[2:])
        return result