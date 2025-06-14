from abc import ABC, abstractmethod

class Content(ABC):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    @abstractmethod
    def getValue(self):
        pass
    
    @abstractmethod
    def setValue(self, value):
        pass