from Formula.EvaluatePostfix import EvaluatePostfix
from Spreadsheet.Content import Content

class FormulaContent(Content):
    def __init__(self, formula: str):
        """
        Initializes a FormulaContent object with a formula string.

        Data Needed:
            - formula (str): The formula string to be stored and evaluated.

        Exceptions:
            - ValueError: If the provided formula is not a valid string or cannot be evaluated.

        Returns:
            - None
        """
        self.formula = formula
        self.expression = []
        pass

    def getValue(self) -> float:
        """
        Retrieves the evaluated numeric value of the formula.

        Data Needed:
            - None (uses self.value)

        Exceptions:
            - None

        Returns:
            - float: The evaluated result of the formula.
        """
        pass

    def getFormula(self) -> str:
        """
        Retrieves the formula string.

        Data Needed:
            - None (uses self.formula)

        Exceptions:
            - None

        Returns:
            - str: The stored formula string.
        """
        pass

    def setValue(self, formula: str) -> None:
        """
        Sets a new formula string for the FormulaContent.

        Data Needed:
            - formula (str): The new formula string to set.

        Exceptions:
            - ValueError: If the provided formula is not a valid string.

        Returns:
            - None
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the FormulaContent object.

        Data Needed:
            - None (uses self.formula and self.value)

        Exceptions:
            - None

        Returns:
            - str: A string describing the formula and its evaluated value.
        """
        pass