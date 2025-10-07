from abc import ABC, abstractmethod
from typing import Any

class DataWriter(ABC):
    @abstractmethod
    def write(self, data: Any, destination: str) -> None:
        pass
    
class DataReader(ABC):
    @abstractmethod
    def read(self, source: str) -> Any:
        pass