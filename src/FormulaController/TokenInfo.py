from src.FormulaController.TokenType import TokenType

class TokenInfo:
    def __init__(self, regex, token):
        """
        Initializes a TokenInfo with a regular expression pattern and token type.
        """
        if not isinstance(regex, str) or not isinstance(token, TokenType):
            raise ValueError("Invalid regex pattern or token type")
        self.regex = regex
        self.token = token