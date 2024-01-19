from decoders.abstract.morse_decoder_base import MorseDecoderBase

class LowercaseMorseDecoder(MorseDecoderBase):
    def decode(self, data: bytes) -> str:
        pass # TODO: Implement