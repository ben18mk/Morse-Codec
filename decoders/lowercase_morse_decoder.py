from consts.parser_consts import MORSE_SPACE
from decoders.abstract.morse_decoder_base import MorseDecoderBase
from parsers.morse_bin_parser import parse_bin_to_morse

class LowercaseMorseDecoder(MorseDecoderBase):
    def decode(self, data: bytes) -> str:
        data_hex = hex(int.from_bytes(data, 'big'))[2:]
        bin_list = list(map(
            lambda x: bin(int(x, 16))[2:].rjust(4, '0'),
            list(data_hex)
        ))
        binary = ''.join(bin_list)
        morse = parse_bin_to_morse(binary).rstrip(MORSE_SPACE)
        print(morse)
        pass # TODO: Implement