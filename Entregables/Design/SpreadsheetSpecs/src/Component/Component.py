from abc import ABC
from abc import abstractmethod

class Component(ABC):
    @abstractmethod
    def getValue(self):
        """
        Retrieves the value of the component.

        Returns:
            - The value of the component (type depends on implementation).
        """
        pass