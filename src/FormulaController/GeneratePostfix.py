from src.FormulaController.TokenType import TokenType


class GeneratePostfix:
    def __init__(self):
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            'SUM': 3,
            'AVERAGE': 3,
            'MAX': 3,
            'MIN': 3
        }
        self.operators = {'+', '-', '*', '/'}

    def infixToPostfix(self, tokens):
        """
        Converts infix tokens to postfix notation using the Shunting Yard algorithm.
        """
        if not tokens:
            raise ValueError("Empty token list")
        
        output = []
        stack = []
        
        for token in tokens:
            if token.token in {TokenType.NUMBER, TokenType.CELL_IDENTIFIER, TokenType.RANGE}:
                output.append(token)
            elif token.token == TokenType.FUNCTION_NAME:
                stack.append(token)
            elif token.token == TokenType.COMMA:
                while stack and stack[-1].sequence != '(':
                    output.append(stack.pop())
                if not stack:
                    raise ValueError("Mismatched parentheses or comma")
            elif token.token == TokenType.OPERATOR:
                while (stack and stack[-1].sequence in self.precedence and
                       self.precedence[stack[-1].sequence] >= self.precedence[token.sequence]):
                    output.append(stack.pop())
                stack.append(token)
            elif token.token == TokenType.OPENING_BRACKET:
                stack.append(token)
            elif token.token == TokenType.CLOSING_BRACKET:
                while stack and stack[-1].sequence != '(':
                    output.append(stack.pop())
                if not stack:
                    raise ValueError("Mismatched parentheses")
                stack.pop()  # Remove '('
                if stack and stack[-1].token == TokenType.FUNCTION_NAME:
                    output.append(stack.pop())  # Add function to output
        
        while stack:
            if stack[-1].sequence == '(':
                raise ValueError("Mismatched parentheses")
            output.append(stack.pop())
        
        return output