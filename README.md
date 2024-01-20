# Morse-Codec
The Morse Codec is a Python library that provides functionality for encoding and decoding text using Morse code. This codec follows a unique approach where the encoding process involves parsing each character to Morse code and the converting the Morse code to bytes. Similarly, during decoding, the library parses bytes input to Morse code and then translates it back to characters.

## Installation
To use the Morse Codec, follow these simple steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/ben18mk/Morse-Codec.git
cd Morse-Codec
```

2. You're ready to use the Morse Codec in your Python projects.

## Usage
### Encoding
To encode text using the Morse Codec, use a Morse encoding class derived from MorseEncoderBase.

For example:
```
from encoders.morse_encoder import MorseEncoder

message_to_encode = 'Hello World'

encoder = MorseEncoder()
encoded_message = encoder.encode(message_to_encode)
print(encoded_message)

# Output: b'U\xdd\x97e\xea\x1a\xea\xd9\xd9y@'
```

### Decoding
To decode bytes using the Morse Codec, use a Morse decoding class derived from MorseDecoderBase, by passing in it's constructor the text-morse parsing technique derived from MorseParserBase.

For example:
```
from decoders.morse_decoder import MorseDecoder

message_to_decode = b'U\xdd\x97e\xea\x1a\xea\xd9\xd9y@'

decoder = MorseDecoder(LowercaseMorseParser())
decoded_message = decoder.decode(message_to_decode)
print(decoded_message)

# Output: 'hello world'
```

In this example LowercaseMorseParser was used as the text-morse parsing technique, therefore the output is in lowercase

## How it works?
### Encode
1. A given text is parsed to Morse code.
2. The Morse code is parse to bits as follows:
```
. (Dit) -> 0b01
- (Dah) -> 0b10

0b11 is placed between characters of the same word.
0b00 represents a space between words
```
3. The binary is then padded by zeros to fill a lenght that can be divided by 8.
4. The padded binary is converted to bytes.

For example:
```
Hello World
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
0101010111011101100101110110010111101010000110101110101011011001110110010111100101000000
01010101 11011101 10010111 01100101 11101010 00011010 11101010 11011001 11011001 01111001 01000000
  0x55     0xDD     0x97     0x65     0xEA     0x1A     0xEA     0xD9     0xD9     0x79     0x40
55 DD 97 65 EA 1A EA D9 D9 79 40
b'U\xdd\x97e\xea\x1a\xea\xd9\xd9y@'
```
Note: Steps 4, 5 and 6 in the example were written to make it easier to visualize

### Decode
1. Given bytes are converted to binary in big endian.
2. The binary is then parsed to Morse code in reverse to the technique above.
3. The Morse code is parsed to text.

For example:
```
b'U\xdd\x97e\xea\x1a\xea\xd9\xd9y@'
0101010111011101100101110110010111101010000110101110101011011001110110010111100101000000
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
Hello World
```