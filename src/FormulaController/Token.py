from src.FormulaController.TokenType import TokenType
import re

class Token:
    def __init__(self, token, sequence):
        """
        Initializes a Token with a token type and its sequence.
        """
        if not isinstance(token, TokenType) or not isinstance(sequence, str):
            raise ValueError("Invalid token type or sequence")
        self.token = token
        self.sequence = sequence

    def evaluate(self, context=None):
        """
        Evaluates the token to compute or validate its value.
        Context is a dict mapping cell references to values for cell evaluation.
        """
        if self.token == TokenType.NUMBER:
            try:
                return float(self.sequence) if '.' in self.sequence else int(self.sequence)
            except ValueError:
                raise ValueError(f"Invalid number token: {self.sequence}")
        elif self.token == TokenType.CELL_IDENTIFIER:
            if context and self.sequence in context:
                return context[self.sequence]
            raise RuntimeError(f"Undefined cell value for: {self.sequence}")
        elif self.token == TokenType.RANGE:
            if context:
                start, end = self.sequence.split(':')
                # Assume range is processed as a list of cell values
                return [context[cell] for cell in self._expand_range(start, end) if cell in context]
            raise RuntimeError(f"Undefined range: {self.sequence}")
        raise ValueError(f"Cannot evaluate token: {self.sequence}")

    def _expand_range(self, start, end):
        """
        Helper to expand a range like A1:A3 into [A1, A2, A3].
        """
        # Simple implementation assuming single-letter column and sequential rows
        col_start, row_start = self._split_cell(start)
        col_end, row_end = self._split_cell(end)
        if col_start != col_end:
            raise ValueError("Range must be in the same column")
        return [f"{col_start}{i}" for i in range(int(row_start), int(row_end) + 1)]

    def _split_cell(self, cell):
        """
        Splits cell reference like A1 into (A, 1).
        """
        match = re.match(r'([A-Z]+)(\d+)', cell)
        if not match:
            raise ValueError(f"Invalid cell reference: {cell}")
        return match.group(1), match.group(2)