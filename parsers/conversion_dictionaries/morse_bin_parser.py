# CR: Change this file name

from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from utils.collection_utils import reversed_dict

bin_to_morse = {
    '00': MORSE_SPACE,
    '01': '.',
    '10': '-',
    '11': MORSE_SEPARATOR
}
morse_to_bin = reversed_dict(bin_to_morse)

"""
CR: SRP-Violation, Coupling...
    parse_morse_to_bin() and parse_bin_to_morse() should
    be taked out to a class or another module 
"""

def parse_morse_to_bin(morse: str) -> str:
    bin_list = list(map(lambda item: morse_to_bin[item], list(morse)))
    result = ''.join(bin_list)
    return result + (8 - len(result) % 8) * '0' # 0 Right Padding


def parse_bin_to_morse(bin_string: str) -> str:
    two_bits = [bin_string[i:i+2] for i in range(0, len(bin_string), 2)]
    morse_items = list(map(
        lambda two_bit: bin_to_morse[two_bit],
        two_bits
    ))
    return ''.join(morse_items)