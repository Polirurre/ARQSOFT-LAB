from src.FormulaController.TokenType import TokenType


class PostfixEvaluator:
    def __init__(self):
        self.functions = {
            'SUM': lambda args: sum(args),
            'AVERAGE': lambda args: sum(args) / len(args) if args else 0,
            'MAX': lambda args: max(args) if args else float('-inf'),
            'MIN': lambda args: min(args) if args else float('inf')
        }

    def evaluate(self, postfix, context=None):
        """
        Evaluates a postfix expression to compute the final result.
        Context is a dict mapping cell references to values.
        """
        if not postfix:
            raise ValueError("Empty postfix expression")
        
        stack = []
        
        for token in postfix:
            if token.token in {TokenType.NUMBER, TokenType.CELL_IDENTIFIER}:
                stack.append(token.evaluate(context))
            elif token.token == TokenType.RANGE:
                values = token.evaluate(context)
                stack.append(values)
            elif token.token == TokenType.OPERATOR:
                if len(stack) < 2:
                    raise ValueError("Insufficient operands for operator")
                b = stack.pop()
                a = stack.pop()
                if isinstance(a, list) or isinstance(b, list):
                    raise ValueError("Operators not supported for ranges")
                if token.sequence == '+':
                    stack.append(a + b)
                elif token.sequence == '-':
                    stack.append(a - b)
                elif token.sequence == '*':
                    stack.append(a * b)
                elif token.sequence == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)
            elif token.token == TokenType.FUNCTION_NAME:
                if len(stack) < 1:
                    raise ValueError("Insufficient arguments for function")
                args = stack.pop()
                if not isinstance(args, list):
                    args = [args]
                if token.sequence in self.functions:
                    stack.append(self.functions[token.sequence](args))
                else:
                    raise ValueError(f"Unknown function: {token.sequence}")
        
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")
        
        return stack[0]