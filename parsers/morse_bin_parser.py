from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from utils.collection_utils import reversed_dict

bin_to_morse = {
    '00': MORSE_SPACE,
    '01': '.',
    '10': '-',
    '11': MORSE_SEPARATOR
}
morse_to_bin = reversed_dict(bin_to_morse)


def parse_morse_to_bin(morse: str) -> str:
    bin_list = list(map(lambda item: morse_to_bin[item], list(morse)))
    result = ''.join(bin_list)
    return result + (8 - len(result) % 8) * '0' # 0 Right Padding