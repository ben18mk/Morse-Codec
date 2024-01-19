from abc import ABC, abstractclassmethod

class MorseDecoderBase(ABC):
    @abstractclassmethod
    def decode(self, data: bytes) -> str:
        pass