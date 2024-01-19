from consts.parser_consts import MORSE_SEPARATOR, MORSE_SPACE
from utils.collection_utils import reversed_dict

bin_to_morse = {
    '00': MORSE_SPACE,
    '01': '.',
    '10': '-',
    '11': MORSE_SEPARATOR
}
morse_to_bin = reversed_dict(bin_to_morse)