def reversed_dict(dictionary: dict) -> dict:
    return { value: key for key, value in dictionary.items() }