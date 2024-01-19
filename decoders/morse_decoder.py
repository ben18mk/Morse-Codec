from consts.parser_consts import MORSE_SPACE
from decoders.abstract.morse_decoder_base import MorseDecoderBase
from parsers.text_morse_parsers.abstract.morse_parser_base import MorseParserBase
from parsers.morse_bin_parsers.morse_bin_parser import parse_bin_to_morse

class MorseDecoder(MorseDecoderBase):
    def __init__(self, morse_parser: MorseParserBase):
        super().__init__(morse_parser)


    def __hex_nibble_to_bin(self, hex_nibble: str):
        return bin(int(hex_nibble, 16))[2:].rjust(4, '0')


    def decode(self, data: bytes) -> str:
        data_hex = hex(int.from_bytes(data, 'big'))[2:]
        bin_list = list(map(
            self.__hex_nibble_to_bin,
            list(data_hex)
        ))
        binary = ''.join(bin_list)
        morse = parse_bin_to_morse(binary).rstrip(MORSE_SPACE)
        result = self._morse_parser.parse_morse_to_text(morse)
        return result