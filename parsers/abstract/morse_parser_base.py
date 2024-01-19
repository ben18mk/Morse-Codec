from abc import ABC, abstractclassmethod

class MorseParserBase(ABC):
    @abstractclassmethod
    def parse_morse_to_text(morse: str) -> str:
        pass