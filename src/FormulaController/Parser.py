from src.FormulaController.TokenType import TokenType
import re

class Parser:
    def __init__(self):
        self.supported_functions = {'SUM', 'AVERAGE', 'MAX', 'MIN'}
        self.operators = {'+', '-', '*', '/'}
        self.current_index = 0
        self.tokens = []

    def next_token(self, tokens, current_index):
        """
        Retrieves the next token and advances the index.
        """
        if current_index < len(tokens):
            return tokens[current_index], current_index + 1
        return None, current_index

    def parse(self, tokens):
        """
        Parses the token list using the visitor pattern to validate syntax.
        """
        if not tokens:
            raise ValueError("Empty token list")
        
        self.tokens = tokens
        self.current_index = 0
        self._parse_expression()
        
        if self.current_index < len(self.tokens):
            raise SyntaxError(f"Unexpected token: {self.tokens[self.current_index].sequence}")
        
        return self.tokens

    def _parse_expression(self):
        """
        Parses an expression, handling operands, operators, and functions.
        """
        expecting_operand = True
        paren_count = 0

        while self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            
            if expecting_operand:
                if token.token in {TokenType.NUMBER, TokenType.CELL_IDENTIFIER, TokenType.RANGE}:
                    self.visit_coordinate(token) if token.token == TokenType.CELL_IDENTIFIER else \
                    self.visit_number(token) if token.token == TokenType.NUMBER else \
                    self.visit_range(token)
                    expecting_operand = False
                elif token.token == TokenType.FUNCTION_NAME:
                    self.visit_function(token)
                    self.current_index += 1
                    if self.current_index >= len(self.tokens) or self.tokens[self.current_index].sequence != '(':
                        raise SyntaxError(f"Expected '(' after function {token.sequence}")
                    self.visit_parenthesis(self.tokens[self.current_index])
                    paren_count += 1
                    self.current_index += 1
                    self._parse_function_args()
                    expecting_operand = False
                elif token.token == TokenType.OPENING_BRACKET:
                    self.visit_parenthesis(token)
                    paren_count += 1
                    self.current_index += 1
                    self._parse_expression()
                else:
                    raise SyntaxError(f"Expected operand, got {token.sequence}")
            else:
                if token.token == TokenType.OPERATOR:
                    self.visit_operator(token)
                    expecting_operand = True
                    self.current_index += 1
                elif token.token == TokenType.CLOSING_BRACKET:
                    if paren_count == 0:
                        raise SyntaxError("Unmatched closing parenthesis")
                    self.visit_parenthesis(token)
                    paren_count -= 1
                    self.current_index += 1
                    return
                elif token.token == TokenType.COMMA:
                    if paren_count == 0:
                        raise SyntaxError("Comma outside function arguments")
                    self.current_index += 1
                    expecting_operand = True
                else:
                    raise SyntaxError(f"Expected operator or ')', got {token.sequence}")

        if paren_count > 0:
            raise SyntaxError("Unmatched opening parenthesis")

    def _parse_function_args(self):
        """
        Parses arguments for a function (e.g., numbers, cells, ranges).
        """
        while self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            if token.token == TokenType.CLOSING_BRACKET:
                self.visit_parenthesis(token)
                self.current_index += 1
                return
            self._parse_expression()
            if self.current_index < len(self.tokens) and self.tokens[self.current_index].token == TokenType.COMMA:
                self.current_index += 1

    def visit_function(self, token):
        """
        Processes a function token.
        """
        if not self.is_function(token.sequence):
            raise SyntaxError(f"Invalid function: {token.sequence}")

    def visit_coordinate(self, token):
        """
        Processes a cell coordinate token.
        """
        if not self.is_coordinate(token.sequence):
            raise SyntaxError(f"Invalid cell coordinate: {token.sequence}")

    def visit_number(self, token):
        """
        Processes a number token.
        """
        if not self.is_number(token.sequence):
            raise SyntaxError(f"Invalid number: {token.sequence}")

    def visit_operator(self, token):
        """
        Processes an operator token.
        """
        if token.sequence not in self.operators:
            raise SyntaxError(f"Invalid operator: {token.sequence}")

    def visit_parenthesis(self, token):
        """
        Processes a parenthesis token.
        """
        if token.sequence not in {'(', ')'}:
            raise SyntaxError(f"Invalid parenthesis: {token.sequence}")

    def visit_range(self, token):
        """
        Processes a range token.
        """
        if not self.is_range(token.sequence):
            raise SyntaxError(f"Invalid range: {token.sequence}")

    def visit_unknown(self, token):
        """
        Processes an unrecognized token.
        """
        raise SyntaxError(f"Unrecognized token: {token.sequence}")

    def is_function(self, token):
        """
        Checks if the token is a function name.
        """
        return token in self.supported_functions

    def is_coordinate(self, token):
        """
        Checks if the token is a cell coordinate.
        """
        return bool(re.match(r'[A-Z]+\d+', token))

    def is_number(self, token):
        """
        Checks if the token is a number.
        """
        return bool(re.match(r'\d+(\.\d+)?', token))

    def is_range(self, token):
        """
        Checks if the token is a range.
        """
        return bool(re.match(r'[A-Z]+\d+:[A-Z]+\d+', token))