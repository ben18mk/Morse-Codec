from abc import ABC, abstractclassmethod

class MorseEncoderBase(ABC):
    @abstractclassmethod
    def Encode(self, text: str) -> bytes:
        pass