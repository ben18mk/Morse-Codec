from abc import ABC, abstractclassmethod

class MorseEncoderBase(ABC):
    @abstractclassmethod
    def encode(self, text: str) -> bytes:
        pass