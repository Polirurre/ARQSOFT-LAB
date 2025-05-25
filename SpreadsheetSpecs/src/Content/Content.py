from abc import abstractmethod


class Content:
    def __init__(self, value):
        """
        Initializes a Content object with a value and a unique identifier.

        Data Needed:
            - value (any): The underlying value or data of the content (ex.: number, string, formula).

        Exceptions:
            - ValueError: If the value is invalid for the content type (to be enforced by subclasses).

        Returns:
            - None
        """
        pass

    @abstractmethod
    def getValue(self):
        """
        Retrieves the evaluated value of the content.

        Data Needed:
            - None (uses self.value)

        Exceptions:
            - ValueError: If the content cannot be evaluated (to be raised by subclasses).
            - RuntimeError: If evaluation fails due to dependencies (to be raised by subclasses).

        Returns:
            - float or int or list: The evaluated value, type depends on the subclass implementation.
        """

    @abstractmethod
    def setValue(self, value):
        """
        Sets the value of the content.

        Data Needed:
            - value (any): The new value to set (ex.: number, string, formula).

        Exceptions:
            - ValueError: If the value is invalid for the content type (to be enforced by subclasses).

        Returns:
            - None
        """