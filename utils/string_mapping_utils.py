from collections.abc import Mapping

def map_chars_through_words(
        text: str,
        words_delimiter: str,
        chars_delimiter: str,
        new_words_delimiter: str,
        new_chars_delimiter: str,
        char_map_function: Mapping):
    
    words = text.split(words_delimiter)
    mapped_words = list(map(
        lambda word: new_chars_delimiter.join(
            list(map(
                char_map_function,
                list(word) if not chars_delimiter else word.split(chars_delimiter)
            ))
        ),
        words
    ))
    return new_words_delimiter.join(mapped_words)

def map_whether_chars_in_collection(text: str, collection: list):
    return list(map(lambda char: char in collection, collection))