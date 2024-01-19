from consts.parser_consts import SEPARATOR, SPACE
from utils.collection_utils import reversed_dict

morse_to_bin = {
    '00': SPACE,
    '01': '.',
    '10': '-',
    '11': SEPARATOR
}
bin_to_morse = reversed_dict(morse_to_bin)