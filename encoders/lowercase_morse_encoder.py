from encoders.abstract.morse_encoder_base import MorseEncoderBase
from parsers.morse_parser import char_to_morse

class LowerCaseMorseEncoder(MorseEncoderBase):
    def encode(self, text: str) -> bytes:
        morse_list = list(map(
            lambda char: char_to_morse[char.upper()],
            list(text)))
        print(morse_list) # DEBUG
        pass # TODO: Implement