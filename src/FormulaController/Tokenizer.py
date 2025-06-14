from src.FormulaController.Token import Token
from src.FormulaController.TokenInfo import TokenInfo
from src.FormulaController.TokenType import TokenType
import re

class Tokenizer:
    def __init__(self):
        self.patterns = [
            TokenInfo(r'\+|-|\*|/', TokenType.OPERATOR),
            TokenInfo(r'[A-Z]+\d+', TokenType.CELL_IDENTIFIER),
            TokenInfo(r'\d+(\.\d+)?', TokenType.NUMBER),
            TokenInfo(r'\(', TokenType.OPENING_BRACKET),
            TokenInfo(r'\)', TokenType.CLOSING_BRACKET),
            TokenInfo(r':', TokenType.COLON),
            TokenInfo(r';', TokenType.SEMI_COLON),
            TokenInfo(r',', TokenType.COMMA),
            TokenInfo(r'SUM|AVERAGE|MAX|MIN', TokenType.FUNCTION_NAME),
            TokenInfo(r'[A-Z]+\d+:[A-Z]+\d+', TokenType.RANGE),
        ]
        self.tokens = []

    def add(self, regex, token):
        """
        Adds a new token type and its associated regular expression pattern.
        """
        self.patterns.append(TokenInfo(regex, token))

    def tokenize(self, formula):
        """
        Tokenizes the input formula into a list of Token objects.
        """
        if not formula or not isinstance(formula, str):
            raise ValueError("Invalid or empty formula")
        
        combined_pattern = '|'.join(f'({info.regex})' for info in self.patterns)
        matches = re.finditer(combined_pattern, formula)
        self.tokens = []
        
        for match in matches:
            token_str = match.group(0)
            for info in self.patterns:
                if re.fullmatch(info.regex, token_str):
                    self.tokens.append(Token(info.token, token_str))
                    break
            else:
                raise SyntaxError(f"Unrecognized token: {token_str}")
        
        if not self.tokens:
            raise ValueError("No valid tokens found in formula")
        
        return self.tokens

    def getTokens(self):
        """
        Retrieves the list of tokenized Token objects.
        """
        return self.tokens