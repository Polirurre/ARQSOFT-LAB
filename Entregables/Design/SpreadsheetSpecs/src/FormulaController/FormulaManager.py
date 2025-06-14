from .Parser import Parser
from .PostFix import GeneratePostfix
from .Tokenizer import Tokenizer

class FormulaManager:
    def __init__(self):
        """
        Initializes the FormulaManager.

        Data Needed:
            - None

        Exceptions:
            - None

        Returns:
            - None
        """
        self.tokenize = Tokenizer()
        self.parse = Parser()
        self.generatePostfix = GeneratePostfix()
        pass

    def computeFormula(self, formula):
        """
        Computes the result of a given formula.

        Data Needed:
            - formula: The formula to compute.

        Exceptions:
            - ValueError: If the formula is invalid.

        Returns:
            - The postfix result of the formula.
        """
