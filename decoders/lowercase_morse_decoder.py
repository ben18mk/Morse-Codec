from decoders.abstract.morse_decoder_base import MorseDecoderBase

class LowercaseMorseDecoder(MorseDecoderBase):
    def decode(self, data: bytes) -> str:
        data_hex = hex(int.from_bytes(data, 'big'))[2:]
        bin_list = list(map(
            lambda x: bin(int(x, 16))[2:].rjust(4, '0'),
            list(data_hex)
        ))
        binary = ''.join(bin_list)
        pass # TODO: Implement